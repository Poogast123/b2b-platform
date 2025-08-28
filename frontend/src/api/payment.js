import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

const getAuthHeaders = () => {
  const token = localStorage.getItem('token');
  return token ? { Authorization: `Bearer ${token}` } : {};
};

const paymentApi = {
  processPayment: async (paymentData) => {
    try {
      const response = await axios.post(`${API_BASE_URL}/payment/process`, paymentData, {
        headers: getAuthHeaders()
      });
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Payment processing failed');
    }
  },

  getTransactions: async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/payment/transactions`, {
        headers: getAuthHeaders()
      });
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to fetch transactions');
    }
  },

  getPaymentMethods: async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/payment/methods`, {
        headers: getAuthHeaders()
      });
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to fetch payment methods');
    }
  },

  addPaymentMethod: async (methodData) => {
    try {
      const response = await axios.post(`${API_BASE_URL}/payment/methods`, methodData, {
        headers: getAuthHeaders()
      });
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to add payment method');
    }
  }
};

export { paymentApi };