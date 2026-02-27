<script setup lang="ts">
import { ref, computed, nextTick, watch, reactive } from 'vue'
import { 
  IconExpand, 
  IconHistory, 
  IconSparkles, 
  IconClose,
  IconBulb,
  IconChevronUp,
  IconChevronDown,
  IconMicrophone,
  IconShortcuts,
  IconAttachment,
  IconSend,
  IconHelpCircle,
  IconInfoCircle
} from '../icons'
import { api } from '../../services/api'

// Message types based on Figma design
type MessageType = 
  | 'text'           // Simple text message
  | 'loadingState'   // Thinking animation
  | 'loadingData'    // Retrieving financial data
  | 'notProcessed'   // Error with retry
  | 'longAnswer'     // Formatted answer with headers/lists
  | 'tablePositive'  // CRUT recommended with table
  | 'tableNegative'  // CRUT not recommended with table
  | 'inputForm'      // Multi-input form for financial data
  | 'input'          // User input request (dropdown)
  | 'inputAmount'    // User input with amount
  | 'inputError'     // Input with error
  | 'inputSubmit'    // Input with submit button
  | 'calendar'       // Date/time selection for booking calls

// Form field definition
interface FormField {
  id: string
  label: string
  type: 'dropdown' | 'amount' | 'text'
  placeholder?: string
  options?: string[]
  required?: boolean
  minValue?: number
  errorMessage?: string
}

// Table data structure for comparison tables
interface TableData {
  headers: string[]
  rows: {
    label: string
    values: string[]
    highlight?: boolean
  }[]
}

// Message structure
interface Message {
  id: number
  role: 'user' | 'assistant'
  type: MessageType
  content: string
  displayedContent?: string
  isStreaming?: boolean
  actions?: string[]
  title?: string
  subtitle?: string
  tableData?: TableData
  howItWorks?: string[]
  howToSetup?: string
  inputLabel?: string
  inputDescription?: string
  inputValue?: string
  inputError?: string
  savings?: string
  formFields?: FormField[]
  formId?: number
}

// Form state for collecting user inputs
interface FormState {
  assetType: string
  assetValue: string
  payoutRate: string
  charity: string
  beneficiaries: string
  errors: Record<string, string>
}

const props = defineProps<{
  isOpen: boolean
}>()

const emit = defineEmits<{
  close: []
}>()

const inputMessage = ref('')
const showSuggestions = ref(true)
const messages = ref<Message[]>([])
const isThinking = ref(false)
const thinkingMessage = ref('Thinking')
const messagesContainer = ref<HTMLElement | null>(null)

// Tooltip content
const tooltips = {
  assetType: 'Select the type of asset you want to contribute. Different assets have varying tax implications and eligibility.',
  assetValue: 'Enter the current market value of your asset. Minimum $10,000 required for CRUT eligibility.'
}

// Form state management
const formState = reactive<FormState>({
  assetType: 'Stock Options',
  assetValue: '',
  payoutRate: '4% for 24 months',
  charity: 'Doctors Without Borders',
  beneficiaries: 'Family Members',
  errors: {}
})

const hasInput = computed(() => inputMessage.value.trim().length > 0)
const hasMessages = computed(() => messages.value.length > 0)
const hasFormErrors = computed(() => Object.keys(formState.errors).length > 0)

// Calendar state for booking calls
const calendarState = reactive({
  currentMonth: new Date().getMonth(),
  currentYear: new Date().getFullYear(),
  selectedDate: null as Date | null,
  selectedTime: null as string | null,
  availableTimes: ['9:00 AM', '10:00 AM', '11:00 AM', '2:00 PM', '3:00 PM', '4:00 PM']
})

// Calendar helper functions
const monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
const dayNames = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']

function getDaysInMonth(year: number, month: number): number {
  return new Date(year, month + 1, 0).getDate()
}

function getFirstDayOfMonth(year: number, month: number): number {
  const day = new Date(year, month, 1).getDay()
  return day === 0 ? 6 : day - 1 // Convert to Monday-based (0 = Monday)
}

function getCalendarDays(): number[] {
  const daysInMonth = getDaysInMonth(calendarState.currentYear, calendarState.currentMonth)
  const firstDay = getFirstDayOfMonth(calendarState.currentYear, calendarState.currentMonth)
  
  const days: number[] = []
  
  // Previous month days
  const prevMonth = calendarState.currentMonth === 0 ? 11 : calendarState.currentMonth - 1
  const prevYear = calendarState.currentMonth === 0 ? calendarState.currentYear - 1 : calendarState.currentYear
  const daysInPrevMonth = getDaysInMonth(prevYear, prevMonth)
  
  for (let i = firstDay - 1; i >= 0; i--) {
    days.push(-(daysInPrevMonth - i)) // Negative for prev month days
  }
  
  // Current month days
  for (let i = 1; i <= daysInMonth; i++) {
    days.push(i)
  }
  
  // Next month days to fill the grid (6 rows * 7 days = 42)
  const remainingDays = 42 - days.length
  for (let i = 1; i <= remainingDays; i++) {
    days.push(-i - 100) // Negative offset for next month
  }
  
  return days
}

function isToday(day: number): boolean {
  if (day <= 0) return false
  const today = new Date()
  return day === today.getDate() && 
         calendarState.currentMonth === today.getMonth() && 
         calendarState.currentYear === today.getFullYear()
}

function isSelected(day: number): boolean {
  if (day <= 0 || !calendarState.selectedDate) return false
  return day === calendarState.selectedDate.getDate() && 
         calendarState.currentMonth === calendarState.selectedDate.getMonth() && 
         calendarState.currentYear === calendarState.selectedDate.getFullYear()
}

function isPastDate(day: number): boolean {
  if (day <= 0) return true
  const date = new Date(calendarState.currentYear, calendarState.currentMonth, day)
  const today = new Date()
  today.setHours(0, 0, 0, 0)
  return date < today
}

function selectDate(day: number) {
  if (day <= 0 || isPastDate(day)) return
  calendarState.selectedDate = new Date(calendarState.currentYear, calendarState.currentMonth, day)
  calendarState.selectedTime = null
}

function selectTime(time: string) {
  calendarState.selectedTime = time
}

function prevMonth() {
  if (calendarState.currentMonth === 0) {
    calendarState.currentMonth = 11
    calendarState.currentYear--
  } else {
    calendarState.currentMonth--
  }
}

function nextMonth() {
  if (calendarState.currentMonth === 11) {
    calendarState.currentMonth = 0
    calendarState.currentYear++
  } else {
    calendarState.currentMonth++
  }
}

function confirmBooking() {
  if (!calendarState.selectedDate || !calendarState.selectedTime) return
  
  const formattedDate = calendarState.selectedDate.toLocaleDateString('en-US', { 
    weekday: 'long', 
    year: 'numeric', 
    month: 'long', 
    day: 'numeric' 
  })
  
  const confirmMessage: Message = {
    id: Date.now(),
    role: 'assistant',
    type: 'text',
    content: `Your call has been scheduled for ${formattedDate} at ${calendarState.selectedTime}. We'll send you a confirmation email with the meeting details.`,
    actions: ['View my scheduled calls', 'Reschedule']
  }
  messages.value.push(confirmMessage)
  
  // Reset calendar state
  calendarState.selectedDate = null
  calendarState.selectedTime = null
  
  scrollToBottom()
}

// Helper to check if an action is "Set up a call"
function isSetupCallAction(action: string): boolean {
  return action.toLowerCase().includes('set up a call') || action.toLowerCase().includes('setup a call')
}

const suggestedPrompts = [
  'What is a Charitable Remainder Unitrust (CRUT)?',
  'Is a Charitable Remainder Unitrust (CRUT) the correct fit for my investement strategy?',
]

// Scroll to bottom of messages
function scrollToBottom() {
  nextTick(() => {
    if (messagesContainer.value) {
      messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
    }
  })
}

// Stream text word by word
async function streamText(messageIndex: number, fullText: string) {
  const words = fullText.split(' ')
  let currentText = ''
  const message = messages.value[messageIndex]
  if (!message) return
  
  for (let i = 0; i < words.length; i++) {
    currentText += (i === 0 ? '' : ' ') + words[i]
    message.displayedContent = currentText
    scrollToBottom()
    // Random delay between 20-60ms for natural feel
    await new Promise(resolve => setTimeout(resolve, 20 + Math.random() * 40))
  }
  
  message.isStreaming = false
}

// Send message to AI
async function sendMessage(text: string) {
  if (!text.trim()) return
  
  // Add user message
  const userMessage: Message = {
    id: Date.now(),
    role: 'user',
    type: 'text',
    content: text
  }
  messages.value.push(userMessage)
  inputMessage.value = ''
  scrollToBottom()
  
  // Show thinking state
  isThinking.value = true
  scrollToBottom()
  
  try {
    // Call API
    const response = await api.aiChat(text)
    isThinking.value = false
    
    // Parse response data and determine message type
    const responseData = response.data
    const messageType = responseData.messageType as MessageType || 'text'
    
    // Add AI message
    const aiMessage: Message = {
      id: Date.now() + 1,
      role: 'assistant',
      type: messageType,
      content: responseData.response,
      displayedContent: '',
      isStreaming: messageType === 'text' || messageType === 'longAnswer',
      actions: responseData.actions,
      title: responseData.title,
      subtitle: responseData.subtitle,
      tableData: responseData.tableData,
      howItWorks: responseData.howItWorks,
      howToSetup: responseData.howToSetup,
      savings: responseData.savings
    }
    messages.value.push(aiMessage)
    
    // Start streaming animation for text types
    if (aiMessage.isStreaming) {
      const messageIndex = messages.value.length - 1
      await streamText(messageIndex, responseData.response)
    }
    
  } catch (error) {
    isThinking.value = false
    // Show error message
    const errorMessage: Message = {
      id: Date.now() + 1,
      role: 'assistant',
      type: 'notProcessed',
      content: 'Sorry something went wrong! I was not able to process your request. Do you want me to try again?',
      displayedContent: 'Sorry something went wrong! I was not able to process your request. Do you want me to try again?',
      isStreaming: false,
      actions: ['Retry']
    }
    messages.value.push(errorMessage)
  }
  
  scrollToBottom()
}

function handleRetry() {
  // Re-send the last user message
  const lastUserMessage = [...messages.value].reverse().find(m => m.role === 'user')
  if (lastUserMessage) {
    sendMessage(lastUserMessage.content)
  }
}

// Handle action button clicks (like "Check if it is right for me")
async function handleActionClick(action: string) {
  const actionLower = action.toLowerCase()
  
  if (actionLower.includes('check') && actionLower.includes('right')) {
    // Show loading state for retrieving financial data
    isThinking.value = true
    thinkingMessage.value = 'Retrieving your financial data'
    scrollToBottom()
    
    // Simulate loading time
    await new Promise(resolve => setTimeout(resolve, 1500))
    isThinking.value = false
    
    // Show input form message
    const formMessage: Message = {
      id: Date.now(),
      role: 'assistant',
      type: 'inputForm',
      content: 'We need some financial data from you to analyse if a CRUT will suit you',
      actions: ['What are the different asset types?', 'How is this calculated?'],
      formId: Date.now()
    }
    messages.value.push(formMessage)
    
    // Reset form state
    formState.assetValue = ''
    formState.errors = {}
    
    scrollToBottom()
  } else if (actionLower.includes('re-enter') && actionLower.includes('asset')) {
    // User wants to re-enter asset details - show input form again
    const formMessage: Message = {
      id: Date.now(),
      role: 'assistant',
      type: 'inputForm',
      content: 'Please re-enter your asset details below',
      actions: ['What are the different asset types?', 'How is this calculated?'],
      formId: Date.now()
    }
    messages.value.push(formMessage)
    
    // Reset form state
    formState.assetValue = ''
    formState.errors = {}
    
    scrollToBottom()
  } else if (isSetupCallAction(action)) {
    // Show calendar for booking a call
    const calendarMessage: Message = {
      id: Date.now(),
      role: 'assistant',
      type: 'calendar',
      content: 'You can select a suitable date and time below.'
    }
    messages.value.push(calendarMessage)
    
    // Reset calendar state to current date
    const now = new Date()
    calendarState.currentMonth = now.getMonth()
    calendarState.currentYear = now.getFullYear()
    calendarState.selectedDate = null
    calendarState.selectedTime = null
    
    scrollToBottom()
  } else {
    // For other actions, send as a message
    sendMessage(action)
  }
}

// Validate asset value
function validateAssetValue(value: string): string | null {
  const numValue = parseFloat(value.replace(/[,$]/g, ''))
  if (isNaN(numValue) || numValue < 10000) {
    return 'Asset Value Cannot be less than $10,000'
  }
  return null
}

// Handle form input changes
function handleFormInput(field: string, value: string) {
  (formState as any)[field] = value
  
  // Real-time validation for assetValue
  if (field === 'assetValue') {
    const error = validateAssetValue(value)
    if (error) {
      formState.errors[field] = error
    } else {
      delete formState.errors[field]
    }
  } else {
    // Clear error when user types for other fields
    if (formState.errors[field]) {
      delete formState.errors[field]
    }
  }
}

// Handle form submission
async function handleFormSubmit() {
  // Validate asset value
  const assetError = validateAssetValue(formState.assetValue)
  if (assetError) {
    formState.errors = { assetValue: assetError }
    return
  }
  
  // Clear errors
  formState.errors = {}
  
  // Show thinking state
  isThinking.value = true
  thinkingMessage.value = 'Analysing your investment strategy'
  scrollToBottom()
  
  try {
    // Call API with form data
    const response = await api.aiChat(`Analyze CRUT viability with: Asset Type: ${formState.assetType}, Asset Value: $${formState.assetValue}, Payout Rate: ${formState.payoutRate}, Charity: ${formState.charity}, Beneficiaries: ${formState.beneficiaries}`)
    isThinking.value = false
    
    const responseData = response.data
    const messageType = responseData.messageType as MessageType || 'tablePositive'
    
    // Add AI response
    const aiMessage: Message = {
      id: Date.now() + 1,
      role: 'assistant',
      type: messageType,
      content: responseData.response,
      actions: responseData.actions,
      title: responseData.title,
      tableData: responseData.tableData,
      howToSetup: responseData.howToSetup,
      savings: responseData.savings
    }
    messages.value.push(aiMessage)
    
  } catch (error) {
    isThinking.value = false
    const errorMessage: Message = {
      id: Date.now() + 1,
      role: 'assistant',
      type: 'notProcessed',
      content: 'Sorry something went wrong! I was not able to process your request. Do you want me to try again?',
      actions: ['Retry']
    }
    messages.value.push(errorMessage)
  }
  
  scrollToBottom()
}

function handleSend() {
  if (hasInput.value) {
    sendMessage(inputMessage.value)
  }
}

function handlePromptClick(prompt: string) {
  sendMessage(prompt)
}

// Watch for panel open to reset state if needed
watch(() => props.isOpen, (isOpen) => {
  if (isOpen) {
    scrollToBottom()
  }
})
</script>

<template>
  <Transition name="slide">
    <aside v-if="isOpen" class="ai-panel">
      <!-- Header -->
      <div class="ai-panel__header">
        <div class="ai-panel__header-left">
          <button class="ai-panel__icon-btn">
            <IconExpand :size="24" />
          </button>
          <button class="ai-panel__icon-btn">
            <IconHistory :size="20" />
          </button>
        </div>
        <div class="ai-panel__header-center">
          <IconSparkles :size="20" class="ai-panel__sparkles" />
          <span class="ai-panel__header-title">Ask AI</span>
        </div>
        <div class="ai-panel__header-right">
          <button class="ai-panel__icon-btn" @click="emit('close')">
            <IconClose :size="20" />
          </button>
        </div>
      </div>

      <!-- Message Container -->
      <div ref="messagesContainer" class="ai-panel__content">
        <!-- Welcome Section (shown when no messages) -->
        <div v-if="!hasMessages" class="ai-panel__welcome">
          <div class="ai-panel__avatar">
            <svg width="79" height="79" viewBox="0 0 79 79" fill="none">
              <defs>
                <linearGradient id="avatarGradient1" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" style="stop-color:#818CF8" />
                  <stop offset="50%" style="stop-color:#C084FC" />
                  <stop offset="100%" style="stop-color:#F472B6" />
                </linearGradient>
                <linearGradient id="avatarGradient2" x1="0%" y1="100%" x2="100%" y2="0%">
                  <stop offset="0%" style="stop-color:#60A5FA" />
                  <stop offset="100%" style="stop-color:#A78BFA" />
                </linearGradient>
              </defs>
              <rect x="8" y="24" width="36" height="36" rx="8" fill="url(#avatarGradient1)" />
              <rect x="28" y="16" width="36" height="36" rx="8" fill="url(#avatarGradient2)" opacity="0.7" />
              <rect x="18" y="8" width="24" height="24" rx="6" fill="url(#avatarGradient1)" opacity="0.5" />
            </svg>
          </div>
          <h2 class="ai-panel__welcome-title">Hi There!</h2>
          <p class="ai-panel__welcome-text">
            I'm Sage - an AI assistant designed to help you turn your assets into income. Feel free to ask me anything!
          </p>
        </div>

        <!-- Messages -->
        <div v-else class="ai-panel__messages">
          <div 
            v-for="message in messages" 
            :key="message.id"
            :class="['ai-panel__message', `ai-panel__message--${message.role}`]"
          >
            <!-- User Message -->
            <template v-if="message.role === 'user'">
              <div class="ai-panel__message-bubble ai-panel__message-bubble--user">
                {{ message.content }}
              </div>
            </template>
            
            <!-- AI Messages -->
            <template v-else>
              <!-- Error/Not Processed State -->
              <div v-if="message.type === 'notProcessed'" class="ai-panel__message-ai">
                <div class="ai-panel__message-sender">Sage</div>
                <div class="ai-panel__message-title ai-panel__message-title--error">
                  {{ message.content }}
                </div>
                <div v-if="message.actions" class="ai-panel__message-actions">
                  <button 
                    v-for="action in message.actions" 
                    :key="action"
                    :class="['ai-panel__action-button', { 'ai-panel__action-button--highlighted': isSetupCallAction(action) }]"
                    @click="handleRetry"
                  >
                    {{ action }}
                  </button>
                </div>
              </div>

              <!-- Long Answer with How It Works -->
              <div v-else-if="message.type === 'longAnswer'" class="ai-panel__message-ai">
                <div class="ai-panel__message-sender">Sage</div>
                <div v-if="message.title" class="ai-panel__message-title">{{ message.title }}</div>
                <div class="ai-panel__message-description">
                  {{ message.isStreaming ? message.displayedContent : message.content }}
                  <span v-if="message.isStreaming" class="ai-panel__cursor">|</span>
                </div>
                <div v-if="message.howItWorks && message.howItWorks.length && !message.isStreaming" class="ai-panel__how-it-works">
                  <p class="ai-panel__how-it-works-title">How It Works</p>
                  <ol class="ai-panel__how-it-works-list">
                    <li v-for="(step, idx) in message.howItWorks" :key="idx">{{ step }}</li>
                  </ol>
                </div>
                <div v-if="message.actions && message.actions.length && !message.isStreaming" class="ai-panel__message-actions">
                  <button 
                    v-for="action in message.actions" 
                    :key="action"
                    :class="['ai-panel__action-button', { 'ai-panel__action-button--highlighted': isSetupCallAction(action) }]"
                    @click="handleActionClick(action)"
                  >
                    {{ action }}
                  </button>
                </div>
              </div>

              <!-- Table Positive (CRUT Recommended) -->
              <div v-else-if="message.type === 'tablePositive'" class="ai-panel__message-ai">
                <div class="ai-panel__message-sender">Sage</div>
                <div class="ai-panel__message-title ai-panel__message-title--positive">
                  {{ message.title || 'A CRUT is advised for your investment strategy!' }}
                </div>
                <div v-if="message.savings" class="ai-panel__message-savings">
                  CRUT will help you save <strong>{{ message.savings }}</strong> in taxes!
                </div>
                <div v-if="message.tableData" class="ai-panel__comparison-table">
                  <div class="ai-panel__table-header">
                    <div class="ai-panel__table-cell ai-panel__table-cell--header"></div>
                    <div 
                      v-for="header in message.tableData.headers" 
                      :key="header"
                      class="ai-panel__table-cell ai-panel__table-cell--header"
                    >
                      {{ header }}
                    </div>
                  </div>
                  <div 
                    v-for="row in message.tableData.rows" 
                    :key="row.label"
                    class="ai-panel__table-row"
                  >
                    <div class="ai-panel__table-cell ai-panel__table-cell--label">{{ row.label }}</div>
                    <div 
                      v-for="(value, idx) in row.values" 
                      :key="idx"
                      :class="['ai-panel__table-cell', { 'ai-panel__table-cell--highlight': row.highlight && idx === 0 }]"
                    >
                      {{ value }}
                    </div>
                  </div>
                </div>
                <div v-if="message.howToSetup" class="ai-panel__how-to-setup">
                  <strong>How To Set It Up :</strong> {{ message.howToSetup }}
                </div>
                <div v-if="message.actions && message.actions.length" class="ai-panel__message-actions">
                  <button 
                    v-for="action in message.actions" 
                    :key="action"
                    :class="['ai-panel__action-button', { 'ai-panel__action-button--highlighted': isSetupCallAction(action) }]"
                    @click="handleActionClick(action)"
                  >
                    {{ action }}
                  </button>
                </div>
              </div>

              <!-- Table Negative (CRUT Not Recommended) -->
              <div v-else-if="message.type === 'tableNegative'" class="ai-panel__message-ai">
                <div class="ai-panel__message-sender">Sage</div>
                <div class="ai-panel__message-title ai-panel__message-title--negative">
                  A CRUT is NOT advised for your investment strategy!
                </div>
                <div class="ai-panel__message-description">
                  {{ message.content }}
                </div>
                <div v-if="message.tableData" class="ai-panel__comparison-table">
                  <div class="ai-panel__table-header">
                    <div class="ai-panel__table-cell ai-panel__table-cell--header"></div>
                    <div 
                      v-for="header in message.tableData.headers" 
                      :key="header"
                      class="ai-panel__table-cell ai-panel__table-cell--header"
                    >
                      {{ header }}
                    </div>
                  </div>
                  <div 
                    v-for="row in message.tableData.rows" 
                    :key="row.label"
                    class="ai-panel__table-row"
                  >
                    <div class="ai-panel__table-cell ai-panel__table-cell--label">{{ row.label }}</div>
                    <div 
                      v-for="(value, idx) in row.values" 
                      :key="idx"
                      class="ai-panel__table-cell"
                    >
                      {{ value }}
                    </div>
                  </div>
                </div>
                <div v-if="message.actions && message.actions.length" class="ai-panel__message-actions">
                  <button 
                    v-for="action in message.actions" 
                    :key="action"
                    :class="['ai-panel__action-button', { 'ai-panel__action-button--highlighted': isSetupCallAction(action) }]"
                    @click="handleActionClick(action)"
                  >
                    {{ action }}
                  </button>
                </div>
              </div>

              <!-- Input Form for Financial Data -->
              <div v-else-if="message.type === 'inputForm'" class="ai-panel__message-ai">
                <div class="ai-panel__message-sender">Sage</div>
                <div class="ai-panel__message-description">{{ message.content }}</div>
                
                <div v-if="message.actions && message.actions.length" class="ai-panel__message-actions ai-panel__message-actions--top">
                  <button 
                    v-for="action in message.actions" 
                    :key="action"
                    :class="['ai-panel__action-button', { 'ai-panel__action-button--highlighted': isSetupCallAction(action) }]"
                    @click="handleActionClick(action)"
                  >
                    {{ action }}
                  </button>
                </div>
                
                <!-- Form Fields as Input Cards -->
                <div class="ai-panel__form">
                  <!-- Asset Type Card -->
                  <div class="ai-panel__input-card">
                    <div class="ai-panel__input-card-header">
                      <span class="ai-panel__input-card-label">Asset Type</span>
                      <span class="ai-panel__tooltip-wrapper">
                        <IconHelpCircle :size="14" class="ai-panel__input-card-help" />
                        <span class="ai-panel__tooltip">{{ tooltips.assetType }}</span>
                      </span>
                    </div>
                    <div class="ai-panel__input-card-field">
                      <select v-model="formState.assetType" class="ai-panel__input-card-select">
                        <option>Stock Options</option>
                        <option>Real Estate</option>
                        <option>Cryptocurrency</option>
                        <option>Business Interest</option>
                      </select>
                      <IconChevronDown :size="20" class="ai-panel__input-card-chevron" />
                    </div>
                  </div>
                  
                  <!-- Asset Value Card -->
                  <div :class="['ai-panel__input-card', { 'ai-panel__input-card--error': formState.errors.assetValue }]">
                    <div class="ai-panel__input-card-header">
                      <span class="ai-panel__input-card-label">Asset Value</span>
                      <span class="ai-panel__tooltip-wrapper">
                        <IconInfoCircle :size="14" class="ai-panel__input-card-help" />
                        <span class="ai-panel__tooltip">{{ tooltips.assetValue }}</span>
                      </span>
                    </div>
                    <div class="ai-panel__input-card-field ai-panel__input-card-field--amount">
                      <span class="ai-panel__input-card-currency">$</span>
                      <input 
                        type="text"
                        v-model="formState.assetValue"
                        placeholder="1,000.00"
                        class="ai-panel__input-card-input"
                        @input="handleFormInput('assetValue', ($event.target as HTMLInputElement).value)"
                      />
                      <div class="ai-panel__input-card-suffix">
                        <IconHelpCircle :size="16" class="ai-panel__input-card-help" />
                        <span class="ai-panel__input-card-unit">US $</span>
                        <IconChevronDown :size="20" class="ai-panel__input-card-chevron" />
                      </div>
                    </div>
                    <div v-if="formState.errors.assetValue" class="ai-panel__input-card-error">
                      {{ formState.errors.assetValue }}
                    </div>
                  </div>
                  
                  <!-- Payout Rate Card -->
                  <div class="ai-panel__input-card">
                    <div class="ai-panel__input-card-header">
                      <span class="ai-panel__input-card-label">Payout Rate</span>
                      <IconInfoCircle :size="14" class="ai-panel__input-card-help" />
                    </div>
                    <p class="ai-panel__input-card-description">Payout rates are affected by length of investement</p>
                    <div class="ai-panel__input-card-field">
                      <select v-model="formState.payoutRate" class="ai-panel__input-card-select">
                        <option>4% for 24 months</option>
                        <option>5% for 36 months</option>
                        <option>6% for 48 months</option>
                        <option>7% for 60 months</option>
                      </select>
                      <IconHelpCircle :size="16" class="ai-panel__input-card-help" />
                      <IconChevronDown :size="20" class="ai-panel__input-card-chevron" />
                    </div>
                  </div>
                  
                  <!-- Charity Card -->
                  <div class="ai-panel__input-card">
                    <div class="ai-panel__input-card-header">
                      <span class="ai-panel__input-card-label">Charity</span>
                      <IconHelpCircle :size="14" class="ai-panel__input-card-help" />
                    </div>
                    <div class="ai-panel__input-card-field">
                      <select v-model="formState.charity" class="ai-panel__input-card-select">
                        <option>Doctors Without Borders</option>
                        <option>Red Cross</option>
                        <option>UNICEF</option>
                        <option>World Wildlife Fund</option>
                      </select>
                      <IconHelpCircle :size="16" class="ai-panel__input-card-help" />
                      <IconChevronDown :size="20" class="ai-panel__input-card-chevron" />
                    </div>
                  </div>
                  
                  <!-- Beneficiaries Card -->
                  <div class="ai-panel__input-card">
                    <div class="ai-panel__input-card-header">
                      <span class="ai-panel__input-card-label">Beneficiaries</span>
                    </div>
                    <div class="ai-panel__input-card-field">
                      <select v-model="formState.beneficiaries" class="ai-panel__input-card-select">
                        <option>Family Members</option>
                        <option>Spouse Only</option>
                        <option>Children Only</option>
                        <option>Trust</option>
                      </select>
                      <IconHelpCircle :size="16" class="ai-panel__input-card-help" />
                      <IconChevronDown :size="20" class="ai-panel__input-card-chevron" />
                    </div>
                  </div>
                </div>
                
                <!-- Submit Button -->
                <button v-if="!hasFormErrors" class="ai-panel__form-submit" @click="handleFormSubmit">
                  Submit
                </button>
              </div>

              <!-- Calendar for Booking Calls -->
              <div v-else-if="message.type === 'calendar'" class="ai-panel__message-ai">
                <div class="ai-panel__message-sender">Sage</div>
                <div class="ai-panel__message-description">{{ message.content }}</div>
                
                <div class="ai-panel__calendar">
                  <div class="ai-panel__calendar-header">
                    <button class="ai-panel__calendar-nav" @click="prevMonth">
                      <span>&lt;</span>
                    </button>
                    <span class="ai-panel__calendar-title">{{ monthNames[calendarState.currentMonth] }} {{ calendarState.currentYear }}</span>
                    <button class="ai-panel__calendar-nav" @click="nextMonth">
                      <span>&gt;</span>
                    </button>
                  </div>
                  
                  <div class="ai-panel__calendar-days">
                    <div v-for="day in dayNames" :key="day" class="ai-panel__calendar-day-name">{{ day }}</div>
                  </div>
                  
                  <div class="ai-panel__calendar-grid">
                    <button 
                      v-for="(day, idx) in getCalendarDays()" 
                      :key="idx"
                      :class="[
                        'ai-panel__calendar-date',
                        { 'ai-panel__calendar-date--other': day <= 0 },
                        { 'ai-panel__calendar-date--today': isToday(day) },
                        { 'ai-panel__calendar-date--selected': isSelected(day) },
                        { 'ai-panel__calendar-date--disabled': isPastDate(day) }
                      ]"
                      :disabled="day <= 0 || isPastDate(day)"
                      @click="selectDate(day)"
                    >
                      {{ day > 0 ? day : (day > -100 ? Math.abs(day) : Math.abs(day) - 100) }}
                    </button>
                  </div>
                  
                  <!-- Time Selection (shown after date is selected) -->
                  <div v-if="calendarState.selectedDate" class="ai-panel__time-selection">
                    <div class="ai-panel__time-label">Select a time:</div>
                    <div class="ai-panel__time-grid">
                      <button 
                        v-for="time in calendarState.availableTimes" 
                        :key="time"
                        :class="[
                          'ai-panel__time-slot',
                          { 'ai-panel__time-slot--selected': calendarState.selectedTime === time }
                        ]"
                        @click="selectTime(time)"
                      >
                        {{ time }}
                      </button>
                    </div>
                  </div>
                  
                  <!-- Confirm Button -->
                  <button 
                    v-if="calendarState.selectedDate && calendarState.selectedTime"
                    class="ai-panel__calendar-confirm"
                    @click="confirmBooking"
                  >
                    Confirm Booking
                  </button>
                </div>
              </div>

              <!-- Default Text Message -->
              <div v-else class="ai-panel__message-ai">
                <div class="ai-panel__message-sender">Sage</div>
                <div class="ai-panel__message-content">
                  {{ message.isStreaming ? message.displayedContent : message.content }}
                  <span v-if="message.isStreaming" class="ai-panel__cursor">|</span>
                </div>
                <div v-if="message.actions && message.actions.length && !message.isStreaming" class="ai-panel__message-actions">
                  <button 
                    v-for="action in message.actions" 
                    :key="action"
                    :class="['ai-panel__action-button', { 'ai-panel__action-button--highlighted': isSetupCallAction(action) }]"
                    @click="handleActionClick(action)"
                  >
                    {{ action }}
                  </button>
                </div>
              </div>
            </template>
          </div>
          
          <!-- Thinking Indicator -->
          <div v-if="isThinking" class="ai-panel__message ai-panel__message--assistant">
            <div class="ai-panel__message-ai">
              <div class="ai-panel__message-sender">Sage</div>
              <div class="ai-panel__thinking">
                <span class="ai-panel__thinking-text">{{ thinkingMessage }}</span>
                <span class="ai-panel__thinking-dots">
                  <span class="ai-panel__dot"></span>
                  <span class="ai-panel__dot"></span>
                  <span class="ai-panel__dot"></span>
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Bottom Section -->
      <div class="ai-panel__bottom">
        <!-- Suggested Prompts (shown when no messages) -->
        <div v-if="!hasMessages" class="ai-panel__prompts">
          <div class="ai-panel__prompts-header">
            <div class="ai-panel__prompts-title">
              <IconBulb :size="20" class="ai-panel__prompts-icon" />
              <span>Suggested Prompts</span>
            </div>
            <button class="ai-panel__icon-btn" @click="showSuggestions = !showSuggestions">
              <IconChevronUp :size="24" :class="{ 'ai-panel__chevron--collapsed': !showSuggestions }" />
            </button>
          </div>
          <div v-if="showSuggestions" class="ai-panel__prompts-list">
            <template v-for="(prompt, index) in suggestedPrompts" :key="index">
              <button class="ai-panel__prompt-item" @click="handlePromptClick(prompt)">
                {{ prompt }}
              </button>
              <div class="ai-panel__prompt-divider" />
            </template>
          </div>
        </div>

        <!-- Message Bar -->
        <div class="ai-panel__message-bar">
          <div class="ai-panel__textarea-wrapper">
            <textarea
              v-model="inputMessage"
              placeholder="Ask me anything..."
              class="ai-panel__textarea"
              rows="4"
              @keydown.enter.exact.prevent="handleSend"
            />
            <div class="ai-panel__input-buttons">
              <button class="ai-panel__mic-btn">
                <IconMicrophone :size="24" />
              </button>
              <button 
                v-if="hasInput" 
                class="ai-panel__send-btn" 
                @click="handleSend"
              >
                <IconSend :size="20" />
              </button>
            </div>
          </div>
          <div class="ai-panel__actions">
            <button class="ai-panel__action-btn ai-panel__action-btn--left">
              <span>{{ hasInput ? 'Generate Reply' : 'Suggested questions' }}</span>
              <IconChevronDown v-if="hasInput" :size="24" />
              <IconChevronUp v-else :size="24" class="ai-panel__chevron-rotated" />
            </button>
            <div class="ai-panel__actions-right">
              <button class="ai-panel__action-btn">
                <IconShortcuts :size="24" />
                <span>Shortcuts</span>
              </button>
              <button class="ai-panel__action-btn">
                <IconAttachment :size="24" />
                <span>Attach</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </aside>
  </Transition>
</template>

<style scoped>
.ai-panel {
  width: 459px;
  min-width: 459px;
  height: 100vh;
  background: var(--surface-card-bg);
  border-left: 1px solid #f0f0f0;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  flex-shrink: 0;
}

/* Header */
.ai-panel__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 80px;
  padding: 12px 24px;
  background: white;
  border-bottom: 1px solid #f0f0f0;
  border-right: 1px solid #f0f0f0;
  flex-shrink: 0;
}

.ai-panel__header-left {
  display: flex;
  align-items: center;
  gap: 8px;
}

.ai-panel__header-center {
  display: flex;
  align-items: center;
  gap: 8px;
}

.ai-panel__sparkles {
  color: var(--text-primary);
}

.ai-panel__header-title {
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  font-size: 16px;
  color: #212121;
}

.ai-panel__header-right {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  width: 56px;
}

.ai-panel__icon-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  background: none;
  border: none;
  color: var(--text-secondary);
  padding: 2px;
  cursor: pointer;
  border-radius: 4px;
}

.ai-panel__icon-btn:hover {
  color: var(--text-primary);
  background: var(--surface-card-item-bg);
}

/* Content / Message Container */
.ai-panel__content {
  flex: 1;
  display: flex;
  flex-direction: column;
  padding: 24px;
  background: var(--surface-card-bg);
  overflow-y: auto;
}

.ai-panel__welcome {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  flex: 1;
  gap: 4px;
  text-align: center;
}

.ai-panel__avatar {
  display: flex;
  justify-content: center;
  margin-bottom: 4px;
  transform: scaleY(-1) rotate(180deg);
}

.ai-panel__welcome-title {
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-size: 18px;
  line-height: 20px;
  color: var(--text-primary);
  margin: 0;
}

.ai-panel__welcome-text {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-size: 14px;
  line-height: 18px;
  color: var(--text-secondary);
  margin: 0;
  text-align: center;
  max-width: 320px;
}

/* Messages */
.ai-panel__messages {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.ai-panel__message {
  display: flex;
  flex-direction: column;
}

.ai-panel__message--user {
  align-items: flex-end;
}

.ai-panel__message--assistant {
  align-items: flex-start;
}

.ai-panel__message-bubble {
  max-width: 85%;
  padding: 12px 16px;
  border-radius: 16px;
  font-family: 'Inter', sans-serif;
  font-size: 14px;
  line-height: 1.5;
}

.ai-panel__message-bubble--user {
  background: #f3f4f6;
  color: var(--text-primary);
  border-bottom-right-radius: 4px;
}

.ai-panel__message-ai {
  display: flex;
  flex-direction: column;
  gap: 8px;
  max-width: 100%;
}

.ai-panel__message-sender {
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  font-size: 14px;
  color: var(--color-primary-600);
}

.ai-panel__message-content {
  font-family: 'Inter', sans-serif;
  font-size: 14px;
  line-height: 1.6;
  color: var(--text-primary);
  white-space: pre-wrap;
}

.ai-panel__cursor {
  display: inline-block;
  animation: blink 0.8s infinite;
  color: var(--color-primary-600);
  font-weight: 300;
}

@keyframes blink {
  0%, 50% { opacity: 1; }
  51%, 100% { opacity: 0; }
}

.ai-panel__message-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 8px;
}

.ai-panel__action-button {
  padding: 6px 12px;
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  font-family: 'Inter', sans-serif;
  font-size: 13px;
  font-weight: 500;
  color: var(--text-primary);
  cursor: pointer;
  transition: all 0.15s ease;
}

.ai-panel__action-button:hover {
  background: #f9fafb;
  border-color: var(--color-primary-600);
  color: var(--color-primary-600);
}

.ai-panel__action-button--primary {
  background: white;
  border-color: var(--color-primary-600);
}

.ai-panel__action-button--highlighted {
  background: white;
  border: 1.5px solid #1f2937;
  font-weight: 600;
}

.ai-panel__action-button--highlighted:hover {
  background: #1f2937;
  border-color: #1f2937;
  color: white;
}

/* Message Titles */
.ai-panel__message-title {
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-size: 14px;
  line-height: 20px;
  color: var(--text-primary);
}

.ai-panel__message-title--positive {
  color: var(--color-primary-600);
}

.ai-panel__message-title--negative {
  color: #dc2626;
}

.ai-panel__message-title--error {
  font-weight: 400;
}

/* Message Description */
.ai-panel__message-description {
  font-family: 'Inter', sans-serif;
  font-size: 14px;
  line-height: 18px;
  color: var(--text-secondary);
}

/* Savings highlight */
.ai-panel__message-savings {
  font-family: 'Inter', sans-serif;
  font-size: 14px;
  line-height: 18px;
  color: var(--text-secondary);
}

.ai-panel__message-savings strong {
  font-weight: 700;
  color: var(--text-primary);
}

/* Comparison Table */
.ai-panel__comparison-table {
  width: 100%;
  max-width: 360px;
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 1px 2px rgba(10, 13, 18, 0.05);
}

.ai-panel__table-header {
  display: grid;
  grid-template-columns: 113px 1fr 1fr;
  background: #fafafa;
  border-bottom: 1px solid #e9eaeb;
}

.ai-panel__table-row {
  display: grid;
  grid-template-columns: 113px 1fr 1fr;
  border-bottom: 1px solid #e5e7eb;
}

.ai-panel__table-row:last-child {
  border-bottom: none;
}

.ai-panel__table-cell {
  padding: 12px;
  font-family: 'Inter', sans-serif;
  font-size: 14px;
  line-height: 20px;
  color: #535862;
}

.ai-panel__table-cell--header {
  font-size: 12px;
  font-weight: 600;
  color: #717680;
  padding: 12px 24px;
}

.ai-panel__table-cell--label {
  font-weight: 600;
  color: var(--text-primary);
}

.ai-panel__table-cell--highlight {
  color: #16a34a;
  font-weight: 500;
}

/* How It Works Section */
.ai-panel__how-it-works {
  font-family: 'Inter', sans-serif;
  font-size: 14px;
  line-height: 18px;
  color: var(--text-secondary);
}

.ai-panel__how-it-works-title {
  font-weight: 600;
  color: var(--text-primary);
  margin: 0 0 4px 0;
}

.ai-panel__how-it-works-list {
  margin: 0;
  padding-left: 21px;
}

.ai-panel__how-it-works-list li {
  margin-bottom: 4px;
}

.ai-panel__how-it-works-list li:last-child {
  margin-bottom: 0;
}

/* How To Setup */
.ai-panel__how-to-setup {
  font-family: 'Inter', sans-serif;
  font-size: 14px;
  line-height: 18px;
  color: var(--text-secondary);
}

/* Form Styles */
.ai-panel__form {
  display: flex;
  flex-direction: column;
  gap: 16px;
  width: 100%;
  margin-top: 8px;
}

/* Input Card Styles - Each field in a message-like card */
.ai-panel__input-card {
  background: #f3f4f6;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  padding: 8px 12px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.ai-panel__input-card--error {
  border-color: #dc2626;
}

.ai-panel__input-card--error .ai-panel__input-card-field {
  border-color: #dc2626;
}

.ai-panel__input-card-header {
  display: flex;
  align-items: center;
  gap: 4px;
}

.ai-panel__input-card-label {
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  font-size: 14px;
  line-height: 18px;
  color: var(--text-primary);
}

.ai-panel__input-card-help {
  color: #9ca3af;
  cursor: help;
  flex-shrink: 0;
}

.ai-panel__tooltip-wrapper {
  position: relative;
  display: inline-flex;
  align-items: center;
}

.ai-panel__tooltip {
  visibility: hidden;
  opacity: 0;
  position: absolute;
  bottom: calc(100% + 8px);
  left: 50%;
  transform: translateX(-50%);
  background: #1f2937;
  color: #fff;
  font-size: 12px;
  line-height: 16px;
  padding: 8px 12px;
  border-radius: 6px;
  white-space: normal;
  width: 200px;
  text-align: center;
  z-index: 1000;
  transition: opacity 0.2s ease, visibility 0.2s ease;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.ai-panel__tooltip::after {
  content: '';
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  border: 6px solid transparent;
  border-top-color: #1f2937;
}

.ai-panel__tooltip-wrapper:hover .ai-panel__tooltip {
  visibility: visible;
  opacity: 1;
}

.ai-panel__input-card-description {
  font-family: 'Inter', sans-serif;
  font-size: 14px;
  line-height: 18px;
  color: #06b6d4;
  margin: 0;
}

.ai-panel__input-card-field {
  position: relative;
  display: flex;
  align-items: center;
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  height: 40px;
  box-shadow: 0 1px 2px rgba(10, 13, 18, 0.05);
}

.ai-panel__input-card-field--amount {
  padding-left: 12px;
}

.ai-panel__input-card-select {
  width: 100%;
  height: 100%;
  padding: 8px 12px;
  padding-right: 70px;
  background: transparent;
  border: none;
  font-family: 'Inter', sans-serif;
  font-size: 16px;
  line-height: 24px;
  color: var(--text-primary);
  appearance: none;
  cursor: pointer;
}

.ai-panel__input-card-select:focus {
  outline: none;
}

.ai-panel__input-card-input {
  flex: 1;
  height: 100%;
  padding: 8px 0;
  padding-right: 100px;
  background: transparent;
  border: none;
  font-family: 'Inter', sans-serif;
  font-size: 16px;
  line-height: 24px;
  color: var(--text-primary);
}

.ai-panel__input-card-input:focus {
  outline: none;
}

.ai-panel__input-card-input::placeholder {
  color: #9ca3af;
}

.ai-panel__input-card-currency {
  font-family: 'Inter', sans-serif;
  font-size: 16px;
  color: var(--text-primary);
  margin-right: 4px;
}

.ai-panel__input-card-suffix {
  position: absolute;
  right: 12px;
  display: flex;
  align-items: center;
  gap: 4px;
}

.ai-panel__input-card-unit {
  font-family: 'Inter', sans-serif;
  font-size: 16px;
  color: var(--text-secondary);
}

.ai-panel__input-card-chevron {
  color: var(--text-secondary);
  flex-shrink: 0;
}

/* Positioning for select fields only (not amount fields) */
.ai-panel__input-card-field:not(.ai-panel__input-card-field--amount) .ai-panel__input-card-help {
  position: absolute;
  right: 36px;
}

.ai-panel__input-card-field:not(.ai-panel__input-card-field--amount) .ai-panel__input-card-chevron {
  position: absolute;
  right: 12px;
}

/* Amount field suffix styling */
.ai-panel__input-card-suffix .ai-panel__input-card-help,
.ai-panel__input-card-suffix .ai-panel__input-card-chevron {
  position: static;
}

.ai-panel__input-card-error {
  background: #ff4a4a;
  color: white;
  font-family: 'Inter', sans-serif;
  font-size: 12px;
  line-height: 16px;
  padding: 4px 12px;
  border-radius: 0 0 8px 8px;
  margin: -6px -12px -8px -12px;
  margin-top: 2px;
}

.ai-panel__form-submit {
  align-self: flex-end;
  padding: 8px 16px;
  background: var(--color-primary-600);
  border: none;
  border-radius: 8px;
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  font-size: 14px;
  color: white;
  cursor: pointer;
  transition: background 0.15s ease;
}

.ai-panel__form-submit:hover {
  background: var(--color-primary-700);
}

/* Calendar Styles */
.ai-panel__calendar {
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  padding: 16px;
  max-width: 280px;
  box-shadow: 0 1px 2px rgba(10, 13, 18, 0.05);
}

.ai-panel__calendar-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
}

.ai-panel__calendar-nav {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  background: none;
  border: none;
  border-radius: 6px;
  color: #717680;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.15s ease;
}

.ai-panel__calendar-nav:hover {
  background: #f3f4f6;
  color: var(--text-primary);
}

.ai-panel__calendar-title {
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-size: 14px;
  color: var(--text-primary);
}

.ai-panel__calendar-days {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 4px;
  margin-bottom: 8px;
}

.ai-panel__calendar-day-name {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 28px;
  font-family: 'Inter', sans-serif;
  font-size: 12px;
  font-weight: 500;
  color: #717680;
}

.ai-panel__calendar-grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 4px;
}

.ai-panel__calendar-date {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  width: 32px;
  height: 32px;
  background: none;
  border: none;
  border-radius: 50%;
  font-family: 'Inter', sans-serif;
  font-size: 13px;
  color: var(--text-primary);
  cursor: pointer;
  transition: all 0.15s ease;
}

.ai-panel__calendar-date:hover:not(:disabled) {
  background: #f3f4f6;
}

.ai-panel__calendar-date--other {
  color: #d1d5db;
}

.ai-panel__calendar-date--today {
  color: var(--color-primary-600);
  font-weight: 600;
}

.ai-panel__calendar-date--today::after {
  content: '';
  position: absolute;
  bottom: 4px;
  width: 4px;
  height: 4px;
  background: var(--color-primary-600);
  border-radius: 50%;
}

.ai-panel__calendar-date--selected {
  background: var(--color-primary-600) !important;
  color: white !important;
  font-weight: 500;
}

.ai-panel__calendar-date--disabled {
  color: #d1d5db;
  cursor: not-allowed;
}

.ai-panel__calendar-date--disabled:hover {
  background: none;
}

/* Time Selection */
.ai-panel__time-selection {
  margin-top: 16px;
  padding-top: 16px;
  border-top: 1px solid #e5e7eb;
}

.ai-panel__time-label {
  font-family: 'Inter', sans-serif;
  font-size: 13px;
  font-weight: 500;
  color: var(--text-primary);
  margin-bottom: 8px;
}

.ai-panel__time-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
}

.ai-panel__time-slot {
  padding: 8px 12px;
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 6px;
  font-family: 'Inter', sans-serif;
  font-size: 12px;
  color: var(--text-primary);
  cursor: pointer;
  transition: all 0.15s ease;
}

.ai-panel__time-slot:hover {
  border-color: var(--color-primary-600);
  color: var(--color-primary-600);
}

.ai-panel__time-slot--selected {
  background: var(--color-primary-600);
  border-color: var(--color-primary-600);
  color: white;
}

.ai-panel__calendar-confirm {
  width: 100%;
  margin-top: 16px;
  padding: 10px 16px;
  background: var(--color-primary-600);
  border: none;
  border-radius: 8px;
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  font-size: 14px;
  color: white;
  cursor: pointer;
  transition: background 0.15s ease;
}

.ai-panel__calendar-confirm:hover {
  background: var(--color-primary-700);
}

.ai-panel__message-actions--top {
  margin-bottom: 8px;
}

/* Thinking Animation */
.ai-panel__thinking {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 10px;
  background: #f3f4f6;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  border-top-left-radius: 0;
}

.ai-panel__thinking-text {
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  font-size: 14px;
  line-height: 20px;
  color: #414651;
}

.ai-panel__thinking-dots {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  height: 8px;
}

.ai-panel__dot {
  width: 4px;
  height: 4px;
  background: var(--color-primary-600);
  border-radius: 50%;
  animation: dotBounce 1.4s infinite ease-in-out;
}

.ai-panel__dot:nth-child(1) { animation-delay: 0s; }
.ai-panel__dot:nth-child(2) { animation-delay: 0.2s; }
.ai-panel__dot:nth-child(3) { animation-delay: 0.4s; }

@keyframes dotBounce {
  0%, 80%, 100% {
    transform: translateY(0);
  }
  40% {
    transform: translateY(-4px);
  }
}

/* Bottom Section */
.ai-panel__bottom {
  display: flex;
  flex-direction: column;
  gap: 24px;
  padding: 0 24px 20px;
  background: white;
  flex-shrink: 0;
}

/* Suggested Prompts */
.ai-panel__prompts {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.ai-panel__prompts-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.ai-panel__prompts-title {
  display: flex;
  align-items: center;
  gap: 4px;
}

.ai-panel__prompts-icon {
  color: var(--text-primary);
}

.ai-panel__prompts-title span {
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  font-size: 14px;
  color: var(--text-primary);
}

.ai-panel__prompts-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.ai-panel__prompt-item {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-size: 14px;
  color: var(--text-secondary);
  background: none;
  border: none;
  padding: 0;
  text-align: left;
  cursor: pointer;
  line-height: 1.4;
}

.ai-panel__prompt-item:hover {
  color: var(--text-primary);
}

.ai-panel__prompt-divider {
  height: 1px;
  width: 100%;
  background: var(--outline-button-neutral);
}

.ai-panel__chevron--collapsed {
  transform: rotate(180deg);
}

/* Message Bar */
.ai-panel__message-bar {
  display: flex;
  flex-direction: column;
  background: #f3f4f6;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  height: 160px;
}

.ai-panel__textarea-wrapper {
  position: relative;
  flex: 1;
  display: flex;
  flex-direction: column;
}

.ai-panel__textarea {
  width: 100%;
  height: 100%;
  flex: 1;
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  padding: 12px 14px;
  padding-right: 48px;
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-size: 16px;
  line-height: 24px;
  color: var(--text-primary);
  resize: none;
  box-shadow: 0 1px 2px rgba(10, 13, 18, 0.05);
  box-sizing: border-box;
}

.ai-panel__textarea::placeholder {
  color: #6b7280;
}

.ai-panel__textarea:focus {
  outline: none;
  border-color: var(--outline-button-focus);
}

.ai-panel__input-buttons {
  position: absolute;
  top: 7px;
  right: 7px;
  display: flex;
  align-items: center;
  gap: 4px;
}

.ai-panel__mic-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  background: none;
  border: none;
  color: #6b7280;
  padding: 6px;
  border-radius: 6px;
  cursor: pointer;
}

.ai-panel__mic-btn:hover {
  color: var(--color-primary-600);
  background: rgba(0, 0, 0, 0.05);
}

.ai-panel__send-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--color-primary-600);
  border: none;
  color: white;
  padding: 6px;
  border-radius: 6px;
  cursor: pointer;
}

.ai-panel__send-btn:hover {
  background: var(--color-primary-700);
}

/* Actions */
.ai-panel__actions {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 8px 12px;
}

.ai-panel__action-btn {
  display: flex;
  align-items: center;
  gap: 2px;
  background: none;
  border: none;
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-size: 12px;
  line-height: 18px;
  color: #535862;
  cursor: pointer;
  padding: 0;
}

.ai-panel__action-btn:hover {
  color: var(--text-primary);
}

.ai-panel__action-btn--left {
  gap: 2px;
}

.ai-panel__chevron-rotated {
  transform: rotate(180deg);
}

.ai-panel__actions-right {
  display: flex;
  align-items: center;
  gap: 12px;
}

.ai-panel__actions-right .ai-panel__action-btn {
  gap: 4px;
}

/* Transitions */
.slide-enter-active,
.slide-leave-active {
  transition: all 0.3s ease;
}

.slide-enter-from,
.slide-leave-to {
  width: 0;
  min-width: 0;
  opacity: 0;
}
</style>
