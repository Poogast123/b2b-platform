import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

const getAuthHeaders = () => {
  const token = localStorage.getItem('token');
  return token ? { Authorization: `Bearer ${token}` } : {};
};

const userApi = {
  getProfile: async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/user/profile`, {
        headers: getAuthHeaders()
      });
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to fetch profile');
    }
  },

  updateProfile: async (profileData) => {
    try {
      const response = await axios.put(`${API_BASE_URL}/user/profile`, profileData, {
        headers: getAuthHeaders()
      });
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to update profile');
    }
  },

  getUsers: async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/user/users`, {
        headers: getAuthHeaders()
      });
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to fetch users');
    }
  },

  deleteUser: async (userId) => {
    try {
      const response = await axios.delete(`${API_BASE_URL}/user/users/${userId}`, {
        headers: getAuthHeaders()
      });
      return response.data;
    } catch (error) {
      throw new Error(error.response?.data?.detail || 'Failed to delete user');
    }
  }
};

export { userApi };