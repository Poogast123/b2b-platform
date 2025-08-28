import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

const getAuthHeaders = () => {
  const token = localStorage.getItem('token');
  return token ? { Authorization: `Bearer ${token}` } : {};
};

const documentApi = {
  uploadDocument: async (formData) => {
    try {
      const response = await axios.post(`${API_BASE_URL}/document/upload`, formData, {
        headers: {
          ...getAuthHeaders(),
          'Content-Type': 'multipart/form-data'
        }
      });
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Document upload failed');
    }
  },

  getDocuments: async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/document/documents`, {
        headers: getAuthHeaders()
      });
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to fetch documents');
    }
  },

  deleteDocument: async (documentId) => {
    try {
      const response = await axios.delete(`${API_BASE_URL}/document/documents/${documentId}`, {
        headers: getAuthHeaders()
      });
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to delete document');
    }
  },

  downloadDocument: async (documentId) => {
    try {
      const response = await axios.get(`${API_BASE_URL}/document/download/${documentId}`, {
        headers: getAuthHeaders(),
        responseType: 'blob'
      });
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to download document');
    }
  }
};

export { documentApi };