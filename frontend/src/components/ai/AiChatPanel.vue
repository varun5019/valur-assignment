<script setup lang="ts">
import { ref } from 'vue'
import BaseIcon from '../ui/BaseIcon.vue'

defineProps<{
  isOpen: boolean
}>()

const emit = defineEmits<{
  close: []
}>()

const inputMessage = ref('')

const suggestedPrompts = [
  'What is a Charitable Remainder Unitrust (CRUT)?',
  'Is a Charitable Remainder Unitrust (CRUT) the correct fit for my investement strategy?',
]
</script>

<template>
  <Transition name="slide">
    <aside v-if="isOpen" class="ai-panel">
      <!-- Header -->
      <div class="ai-panel__header">
        <div class="ai-panel__header-left">
          <BaseIcon name="sparkles" :size="18" class="ai-panel__header-icon" />
          <span class="ai-panel__header-title">Ask AI</span>
        </div>
        <button class="ai-panel__close" @click="emit('close')">
          <BaseIcon name="close" :size="20" />
        </button>
      </div>

      <!-- Content -->
      <div class="ai-panel__content">
        <!-- Welcome Section -->
        <div class="ai-panel__welcome">
          <div class="ai-panel__avatar">
            <svg width="48" height="48" viewBox="0 0 48 48" fill="none">
              <defs>
                <linearGradient id="avatarGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" style="stop-color:#818CF8" />
                  <stop offset="50%" style="stop-color:#C084FC" />
                  <stop offset="100%" style="stop-color:#F472B6" />
                </linearGradient>
              </defs>
              <rect x="4" y="12" width="28" height="28" rx="6" fill="url(#avatarGradient)" />
              <rect x="16" y="8" width="28" height="28" rx="6" fill="url(#avatarGradient)" opacity="0.6" />
            </svg>
          </div>
          <h2 class="ai-panel__welcome-title">Hi There!</h2>
          <p class="ai-panel__welcome-text">
            I'm Sage - an AI assistant designed to help you turn your assets into income. Feel free to ask me anything!
          </p>
        </div>

        <!-- Suggested Prompts -->
        <div class="ai-panel__prompts">
          <div class="ai-panel__prompts-header">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M9 18h6" />
              <path d="M10 22h4" />
              <path d="M15.09 14c.18-.98.65-1.74 1.41-2.5A4.65 4.65 0 0 0 18 8 6 6 0 0 0 6 8c0 1 .23 2.23 1.5 3.5A4.61 4.61 0 0 1 8.91 14" />
            </svg>
            <span>Suggested Prompts</span>
          </div>
          <div class="ai-panel__prompts-list">
            <button
              v-for="(prompt, index) in suggestedPrompts"
              :key="index"
              class="ai-panel__prompt-btn"
              @click="inputMessage = prompt"
            >
              {{ prompt }}
            </button>
          </div>
        </div>
      </div>

      <!-- Input Section -->
      <div class="ai-panel__input-section">
        <div class="ai-panel__input-wrapper">
          <input
            v-model="inputMessage"
            type="text"
            placeholder="Ask me anything..."
            class="ai-panel__input"
          />
          <button class="ai-panel__mic-btn">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z" />
              <path d="M19 10v2a7 7 0 0 1-14 0v-2" />
              <line x1="12" y1="19" x2="12" y2="23" />
              <line x1="8" y1="23" x2="16" y2="23" />
            </svg>
          </button>
        </div>
        <div class="ai-panel__input-actions">
          <button class="ai-panel__action-btn ai-panel__action-btn--primary">
            Generate Reply
            <BaseIcon name="chevron-down" :size="14" />
          </button>
          <div class="ai-panel__action-right">
            <button class="ai-panel__action-btn">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="3" y="3" width="18" height="18" rx="2" />
                <line x1="9" y1="3" x2="9" y2="21" />
              </svg>
              Shortcuts
            </button>
            <button class="ai-panel__action-btn">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M21.44 11.05l-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48" />
              </svg>
              Attach
            </button>
          </div>
        </div>
      </div>
    </aside>
  </Transition>
</template>

<style scoped>
.ai-panel {
  width: 380px;
  min-width: 380px;
  height: 100%;
  background: var(--surface-card-bg);
  border-left: 1px solid var(--outline-button-neutral);
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.ai-panel__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 1.25rem;
  border-bottom: 1px solid var(--outline-button-neutral);
  flex-shrink: 0;
}

.ai-panel__header-left {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  white-space: nowrap;
}

.ai-panel__header-icon {
  color: var(--color-primary-600);
}

.ai-panel__header-title {
  font-size: 0.9375rem;
  font-weight: 600;
  color: var(--text-primary);
}

.ai-panel__close {
  display: flex;
  align-items: center;
  justify-content: center;
  background: none;
  border: none;
  color: var(--color-neutral-400);
  padding: 0.25rem;
  cursor: pointer;
  border-radius: 4px;
}

.ai-panel__close:hover {
  color: var(--text-secondary);
  background: var(--surface-card-item-bg);
}

.ai-panel__content {
  flex: 1;
  overflow-y: auto;
  overflow-x: hidden;
  padding: 2rem 1.25rem;
  min-width: 350px;
}

.ai-panel__welcome {
  text-align: center;
  margin-bottom: 2rem;
}

.ai-panel__avatar {
  display: flex;
  justify-content: center;
  margin-bottom: 1rem;
}

.ai-panel__welcome-title {
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--text-primary);
  margin: 0 0 0.5rem;
}

.ai-panel__welcome-text {
  font-size: 0.875rem;
  color: var(--text-secondary);
  line-height: 1.6;
  margin: 0;
  max-width: 280px;
  margin: 0 auto;
}

.ai-panel__prompts {
  background: var(--surface-message-chat-bg);
  border-radius: 12px;
  padding: 1rem;
}

.ai-panel__prompts-header {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.8125rem;
  font-weight: 600;
  color: var(--color-neutral-700);
  margin-bottom: 0.75rem;
}

.ai-panel__prompts-header svg {
  color: var(--color-neutral-400);
}

.ai-panel__prompts-list {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.ai-panel__prompt-btn {
  background: var(--surface-card-bg);
  border: 1px solid var(--outline-button-neutral);
  border-radius: 8px;
  padding: 0.75rem 1rem;
  font-size: 0.8125rem;
  color: var(--color-neutral-700);
  text-align: left;
  cursor: pointer;
  transition: all 0.15s ease;
  line-height: 1.5;
}

.ai-panel__prompt-btn:hover {
  border-color: var(--outline-button-focus);
  background: var(--color-primary-50);
}

.ai-panel__input-section {
  padding: 1rem 1.25rem;
  border-top: 1px solid var(--outline-button-neutral);
  background: var(--surface-card-bg);
  flex-shrink: 0;
}

.ai-panel__input-wrapper {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: var(--surface-input-subtext-bg);
  border: 1px solid var(--outline-button-neutral);
  border-radius: 10px;
  padding: 0.75rem 1rem;
  margin-bottom: 0.75rem;
}

.ai-panel__input {
  flex: 1;
  min-width: 0;
  background: transparent;
  border: none;
  font-size: 0.875rem;
  color: var(--text-primary);
  outline: none;
}

.ai-panel__input::placeholder {
  color: var(--color-neutral-400);
}

.ai-panel__mic-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  background: none;
  border: none;
  color: var(--color-neutral-400);
  cursor: pointer;
  padding: 0.25rem;
}

.ai-panel__mic-btn:hover {
  color: var(--color-primary-600);
}

.ai-panel__input-actions {
  display: flex;
  align-items: center;
  justify-content: space-between;
  white-space: nowrap;
}

.ai-panel__action-btn {
  display: flex;
  align-items: center;
  gap: 0.375rem;
  background: none;
  border: none;
  font-size: 0.8125rem;
  color: var(--text-secondary);
  cursor: pointer;
  padding: 0.375rem 0.5rem;
  border-radius: 6px;
  white-space: nowrap;
}

.ai-panel__action-btn:hover {
  background: var(--surface-card-item-bg);
  color: var(--color-neutral-700);
}

.ai-panel__action-btn--primary {
  color: var(--color-primary-600);
  font-weight: 500;
}

.ai-panel__action-btn--primary:hover {
  background: var(--color-primary-50);
}

.ai-panel__action-right {
  display: flex;
  align-items: center;
  gap: 0.25rem;
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
