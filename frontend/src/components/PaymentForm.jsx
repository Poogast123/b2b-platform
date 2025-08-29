import React, { useState } from 'react';
import { CreditCard, Calendar, Lock } from 'lucide-react';

const PaymentForm = ({ onSubmit, loading }) => {
  const [formData, setFormData] = useState({
    amount: '',
    cardNumber: '',
    expiryDate: '',
    cvv: '',
    cardHolderName: ''
  });
  const [errors, setErrors] = useState({});

  const handleChange = (e) => {
    let { name, value } = e.target;
    
    // Format card number
    if (name === 'cardNumber') {
      value = value.replace(/\s/g, '').replace(/(.{4})/g, '$1 ').trim();
      if (value.length > 19) value = value.substr(0, 19);
    }
    
    // Format expiry date
    if (name === 'expiryDate') {
      value = value.replace(/\D/g, '').replace(/(\d{2})(\d)/, '$1/$2');
      if (value.length > 5) value = value.substr(0, 5);
    }
    
    // CVV numeric only
    if (name === 'cvv') {
      value = value.replace(/\D/g, '').substr(0, 4);
    }
    
    // Amount numeric with decimals
    if (name === 'amount') {
      value = value.replace(/[^0-9.]/g, '');
    }

    setFormData(prev => ({
      ...prev,
      [name]: value
    }));

    // Clear error when user starts typing
    if (errors[name]) {
      setErrors(prev => ({
        ...prev,
        [name]: ''
      }));
    }
  };

  const validateForm = () => {
    const newErrors = {};
    
    if (!formData.amount || formData.amount <= 0) {
      newErrors.amount = 'Valid amount is required';
    }
    
    if (!formData.cardNumber || formData.cardNumber.replace(/\s/g, '').length !== 16) {
      newErrors.cardNumber = 'Valid card number is required';
    }
    
    if (!formData.expiryDate || formData.expiryDate.length !== 5) {
      newErrors.expiryDate = 'Valid expiry date is required (MM/YY)';
    }
    
    if (!formData.cvv || formData.cvv.length < 3) {
      newErrors.cvv = 'Valid CVV is required';
    }
    
    if (!formData.cardHolderName.trim()) {
      newErrors.cardHolderName = 'Cardholder name is required';
    }
    
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

    const handleSubmit = (e) => {
      e.preventDefault();
      if (validateForm()) {
        onSubmit({
          client: formData.cardHolderName,
          amount: parseFloat(formData.amount),
          reference: `TXN-${Date.now()}`,
          card_number: formData.cardNumber.replace(/\s/g, ''),
          cardholder_name: formData.cardHolderName,
          expiry_date: formData.expiryDate,
          cvv: formData.cvv
        });
      }
    };



  return (
    <form onSubmit={handleSubmit} className="space-y-6">
      <div>
        <label htmlFor="amount" className="block text-sm font-medium text-gray-700 mb-1">
          Amount
        </label>
        <div className="relative">
          <span className="absolute left-3 top-3 text-gray-500 font-medium">$</span>
          <input
            id="amount"
            name="amount"
            type="text"
            value={formData.amount}
            onChange={handleChange}
            className={`w-full pl-8 pr-4 py-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors ${
              errors.amount ? 'border-red-500' : 'border-gray-300'
            }`}
            placeholder="0.00"
          />
        </div>
        {errors.amount && (
          <p className="mt-1 text-sm text-red-600">{errors.amount}</p>
        )}
      </div>

      <div>
        <label htmlFor="cardHolderName" className="block text-sm font-medium text-gray-700 mb-1">
          Cardholder Name
        </label>
        <input
          id="cardHolderName"
          name="cardHolderName"
          type="text"
          value={formData.cardHolderName}
          onChange={handleChange}
          className={`w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors ${
            errors.cardHolderName ? 'border-red-500' : 'border-gray-300'
          }`}
          placeholder="John Doe"
        />
        {errors.cardHolderName && (
          <p className="mt-1 text-sm text-red-600">{errors.cardHolderName}</p>
        )}
      </div>

      <div>
        <label htmlFor="cardNumber" className="block text-sm font-medium text-gray-700 mb-1">
          Card Number
        </label>
        <div className="relative">
          <CreditCard className="absolute left-3 top-3 h-5 w-5 text-gray-400" />
          <input
            id="cardNumber"
            name="cardNumber"
            type="text"
            value={formData.cardNumber}
            onChange={handleChange}
            className={`w-full pl-10 pr-4 py-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors ${
              errors.cardNumber ? 'border-red-500' : 'border-gray-300'
            }`}
            placeholder="1234 5678 9012 3456"
          />
        </div>
        {errors.cardNumber && (
          <p className="mt-1 text-sm text-red-600">{errors.cardNumber}</p>
        )}
      </div>

      <div className="grid grid-cols-2 gap-4">
        <div>
          <label htmlFor="expiryDate" className="block text-sm font-medium text-gray-700 mb-1">
            Expiry Date
          </label>
          <div className="relative">
            <Calendar className="absolute left-3 top-3 h-5 w-5 text-gray-400" />
            <input
              id="expiryDate"
              name="expiryDate"
              type="text"
              value={formData.expiryDate}
              onChange={handleChange}
              className={`w-full pl-10 pr-4 py-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors ${
                errors.expiryDate ? 'border-red-500' : 'border-gray-300'
              }`}
              placeholder="MM/YY"
            />
          </div>
          {errors.expiryDate && (
            <p className="mt-1 text-sm text-red-600">{errors.expiryDate}</p>
          )}
        </div>

        <div>
          <label htmlFor="cvv" className="block text-sm font-medium text-gray-700 mb-1">
            CVV
          </label>
          <div className="relative">
            <Lock className="absolute left-3 top-3 h-5 w-5 text-gray-400" />
            <input
              id="cvv"
              name="cvv"
              type="text"
              value={formData.cvv}
              onChange={handleChange}
              className={`w-full pl-10 pr-4 py-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors ${
                errors.cvv ? 'border-red-500' : 'border-gray-300'
              }`}
              placeholder="123"
            />
          </div>
          {errors.cvv && (
            <p className="mt-1 text-sm text-red-600">{errors.cvv}</p>
          )}
        </div>
      </div>

      <button
        type="submit"
        disabled={loading}
        className="w-full bg-green-600 text-white py-3 px-4 rounded-lg font-medium hover:bg-green-700 focus:ring-2 focus:ring-green-500 focus:ring-offset-2 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
      >
        {loading ? (
          <div className="flex items-center justify-center">
            <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white mr-2"></div>
            Processing Payment...
          </div>
        ) : (
          'Process Payment'
        )}
      </button>
    </form>
  );
};

export default PaymentForm;