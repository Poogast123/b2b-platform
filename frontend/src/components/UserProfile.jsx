import React, { useState, useEffect } from 'react';
import { User, Mail, Phone, MapPin, Calendar, Edit2, Save, X } from 'lucide-react';
import { userApi } from '../api/user';

const UserProfile = () => {
  const [profile, setProfile] = useState(null);
  const [isEditing, setIsEditing] = useState(false);
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState('');
  const [editForm, setEditForm] = useState({});

  useEffect(() => {
    loadProfile();
  }, []);

  const loadProfile = async () => {
    try {
      setLoading(true);
      const data = await userApi.getProfile();
      setProfile(data);
      setEditForm(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleEditToggle = () => {
    setIsEditing(!isEditing);
    if (!isEditing) {
      setEditForm({ ...profile });
    }
    setError('');
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setEditForm(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSave = async () => {
    try {
      setSaving(true);
      const updatedProfile = await userApi.updateProfile(editForm);
      setProfile(updatedProfile);
      setIsEditing(false);
      setError('');
    } catch (err) {
      setError(err.message);
    } finally {
      setSaving(false);
    }
  };

  if (loading) {
    return (
      <div className="bg-white rounded-lg shadow-md p-6">
        <div className="animate-pulse">
          <div className="flex items-center space-x-4 mb-6">
            <div className="w-20 h-20 bg-gray-300 rounded-full"></div>
            <div className="space-y-2">
              <div className="h-6 bg-gray-300 rounded w-32"></div>
              <div className="h-4 bg-gray-300 rounded w-48"></div>
            </div>
          </div>
          <div className="space-y-4">
            <div className="h-4 bg-gray-300 rounded w-full"></div>
            <div className="h-4 bg-gray-300 rounded w-3/4"></div>
            <div className="h-4 bg-gray-300 rounded w-1/2"></div>
          </div>
        </div>
      </div>
    );
  }

  if (!profile) {
    return (
      <div className="bg-white rounded-lg shadow-md p-6">
        <p className="text-red-600">Failed to load profile</p>
        <button 
          onClick={loadProfile}
          className="mt-2 bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors"
        >
          Retry
        </button>
      </div>
    );
  }

  return (
    <div className="bg-white rounded-lg shadow-md overflow-hidden">
      <div className="bg-gradient-to-r from-blue-500 to-teal-500 px-6 py-8 text-white">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-4">
            <div className="w-20 h-20 bg-white/20 rounded-full flex items-center justify-center">
              <User className="h-10 w-10 text-white" />
            </div>
            <div>
              <h2 className="text-2xl font-bold">
                {isEditing ? (
                  <input
                    type="text"
                    name="name"
                    value={editForm.name || ''}
                    onChange={handleInputChange}
                    className="bg-white/20 border border-white/30 rounded px-2 py-1 text-white placeholder-white/70"
                    placeholder="Full Name"
                  />
                ) : (
                  profile.name || 'User Name'
                )}
              </h2>
              <p className="text-white/80">{profile.email}</p>
            </div>
          </div>
          <button
            onClick={isEditing ? handleSave : handleEditToggle}
            disabled={saving}
            className="bg-white/20 hover:bg-white/30 text-white p-2 rounded-lg transition-colors disabled:opacity-50"
          >
            {saving ? (
              <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white"></div>
            ) : isEditing ? (
              <Save className="h-5 w-5" />
            ) : (
              <Edit2 className="h-5 w-5" />
            )}
          </button>
          {isEditing && (
            <button
              onClick={handleEditToggle}
              className="bg-white/20 hover:bg-white/30 text-white p-2 rounded-lg transition-colors ml-2"
            >
              <X className="h-5 w-5" />
            </button>
          )}
        </div>
      </div>

      <div className="p-6 space-y-6">
        {error && (
          <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg">
            {error}
          </div>
        )}

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div className="space-y-1">
            <label className="flex items-center text-sm font-medium text-gray-700">
              <Mail className="h-4 w-4 mr-2" />
              Email
            </label>
            {isEditing ? (
              <input
                type="email"
                name="email"
                value={editForm.email || ''}
                onChange={handleInputChange}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              />
            ) : (
              <p className="text-gray-900">{profile.email}</p>
            )}
          </div>

          <div className="space-y-1">
            <label className="flex items-center text-sm font-medium text-gray-700">
              <Phone className="h-4 w-4 mr-2" />
              Phone
            </label>
            {isEditing ? (
              <input
                type="tel"
                name="phone"
                value={editForm.phone || ''}
                onChange={handleInputChange}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                placeholder="Phone number"
              />
            ) : (
              <p className="text-gray-900">{profile.phone || 'Not provided'}</p>
            )}
          </div>

          <div className="space-y-1">
            <label className="flex items-center text-sm font-medium text-gray-700">
              <MapPin className="h-4 w-4 mr-2" />
              Location
            </label>
            {isEditing ? (
              <input
                type="text"
                name="location"
                value={editForm.location || ''}
                onChange={handleInputChange}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                placeholder="City, Country"
              />
            ) : (
              <p className="text-gray-900">{profile.location || 'Not provided'}</p>
            )}
          </div>

          <div className="space-y-1">
            <label className="flex items-center text-sm font-medium text-gray-700">
              <Calendar className="h-4 w-4 mr-2" />
              Joined
            </label>
            <p className="text-gray-900">
              {profile.createdAt ? new Date(profile.createdAt).toLocaleDateString() : 'Unknown'}
            </p>
          </div>
        </div>

        {isEditing && (
          <div className="space-y-1">
            <label className="block text-sm font-medium text-gray-700">
              Bio
            </label>
            <textarea
              name="bio"
              value={editForm.bio || ''}
              onChange={handleInputChange}
              rows="3"
              className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              placeholder="Tell us about yourself..."
            />
          </div>
        )}

        {!isEditing && profile.bio && (
          <div className="space-y-1">
            <label className="block text-sm font-medium text-gray-700">
              Bio
            </label>
            <p className="text-gray-900">{profile.bio}</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default UserProfile;