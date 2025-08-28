import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  root: '.',              
  build: {
    outDir: 'dist',
  },
    server: {
    proxy: {
      '/auth': 'http://localhost:8000',
      '/user': 'http://localhost:8000',
      '/payment': 'http://localhost:8000',
      '/document': 'http://localhost:8000',
    },
  },
})
