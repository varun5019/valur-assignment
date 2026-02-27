<script setup lang="ts">
import { ref, computed } from 'vue'
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
  IconSend
} from '../icons'

defineProps<{
  isOpen: boolean
}>()

const emit = defineEmits<{
  close: []
}>()

const inputMessage = ref('')
const showSuggestions = ref(true)

const hasInput = computed(() => inputMessage.value.trim().length > 0)

const suggestedPrompts = [
  'What is a Charitable Remainder Unitrust (CRUT)?',
  'Is a Charitable Remainder Unitrust (CRUT) the correct fit for my investement strategy?',
]

function handleSend() {
  if (hasInput.value) {
    // TODO: Handle send message
    console.log('Sending:', inputMessage.value)
    inputMessage.value = ''
  }
}
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
      <div class="ai-panel__content">
        <div class="ai-panel__welcome">
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
      </div>

      <!-- Bottom Section -->
      <div class="ai-panel__bottom">
        <!-- Suggested Prompts -->
        <div class="ai-panel__prompts">
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
              <button class="ai-panel__prompt-item" @click="inputMessage = prompt">
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
              @keydown.enter.ctrl="handleSend"
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
  align-items: center;
  justify-content: center;
  padding: 36px;
  background: var(--surface-card-bg);
  overflow-y: auto;
}

.ai-panel__welcome {
  display: flex;
  flex-direction: column;
  align-items: center;
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
  min-width: 100%;
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
