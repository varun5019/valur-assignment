import axios from 'axios'

const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000/api',
  headers: {
    'Content-Type': 'application/json',
  },
  withCredentials: true,
})

// Request interceptor
apiClient.interceptors.request.use(
  (config) => {
    // You can add auth tokens here
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// Response interceptor
apiClient.interceptors.response.use(
  (response) => {
    return response
  },
  (error) => {
    // Handle errors globally
    console.error('API Error:', error)
    return Promise.reject(error)
  }
)

export default apiClient

// Types
export interface TableData {
  headers: string[]
  rows: {
    label: string
    values: string[]
    highlight?: boolean
  }[]
}

export interface AiChatResponse {
  response: string
  messageType?: string
  title?: string
  subtitle?: string
  actions?: string[]
  tableData?: TableData
  howItWorks?: string[]
  howToSetup?: string
  savings?: string
}

// API functions
export const api = {
  // Health check
  healthCheck: () => apiClient.get('/health/'),
  
  // AI Chat
  aiChat: (message: string) => apiClient.post<AiChatResponse>('/ai/chat/', { message }),
}
