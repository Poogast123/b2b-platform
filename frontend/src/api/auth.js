import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

const authApi = {
  login: async (credentials) => {
    const response = await axios.post(`${API_BASE_URL}/auth/login`, credentials);
    const { access_token } = response.data;

    if (!access_token) {
      throw new Error("No token received from backend");
    }

    // Save token in localStorage
    localStorage.setItem('token', access_token);
    return response.data;
  },

  verifyToken: async () => {
    const token = localStorage.getItem('token');

    if (!token) {
      throw new Error("No token found");
    }

    try {
      const response = await axios.get(`${API_BASE_URL}/auth/verify`, {
        headers: { Authorization: `Bearer ${token}` }
      });
      return response.data; // { status: 'valid', email: ... }
    } catch (err) {
      throw new Error(err.response?.data?.detail || "Token verification failed");
    }
  },

  logout: () => {
    localStorage.removeItem('token');
  }
};

export { authApi };
