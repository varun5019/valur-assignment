<script setup lang="ts">
import TheSidebar from './components/layout/TheSidebar.vue'
import TheHeader from './components/layout/TheHeader.vue'
import AiChatPanel from './components/ai/AiChatPanel.vue'
import { useAppStore } from './stores/app'

const appStore = useAppStore()
</script>

<template>
  <div class="app-layout">
    <TheSidebar />
    <div class="app-layout__main">
      <TheHeader :breadcrumb="['Dashboard', 'Home']" />
      <main class="app-layout__content">
        <router-view />
      </main>
    </div>
    
    <!-- AI Chat Panel (Side Pane) -->
    <AiChatPanel 
      :is-open="appStore.isAiPanelOpen" 
      @close="appStore.closeAiPanel" 
    />
  </div>
</template>

<style scoped>
.app-layout {
  display: flex;
  min-height: 100vh;
}

.app-layout__main {
  flex: 1;
  display: flex;
  flex-direction: column;
  min-width: 0;
}

.app-layout__content {
  flex: 1;
  overflow-y: auto;
  min-width: 0;
}
</style>

