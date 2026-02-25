import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useAppStore = defineStore('app', () => {
  const apiStatus = ref<string>('unknown')
  const isLoading = ref<boolean>(false)
  const isAiPanelOpen = ref<boolean>(false)

  function setApiStatus(status: string) {
    apiStatus.value = status
  }

  function setLoading(loading: boolean) {
    isLoading.value = loading
  }

  function openAiPanel() {
    isAiPanelOpen.value = true
  }

  function closeAiPanel() {
    isAiPanelOpen.value = false
  }

  function toggleAiPanel() {
    isAiPanelOpen.value = !isAiPanelOpen.value
  }

  return { 
    apiStatus, 
    isLoading, 
    isAiPanelOpen,
    setApiStatus, 
    setLoading,
    openAiPanel,
    closeAiPanel,
    toggleAiPanel
  }
})
