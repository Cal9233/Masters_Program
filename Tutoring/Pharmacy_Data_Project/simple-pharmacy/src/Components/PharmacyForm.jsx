import React, {useState} from 'react'

const PharmacyForm = () => {
    const [data, setData] = useState({
        ssn: '',
        first_name: '',
        last_name: '',
        medication: '',
        dosage: ''
    })
    const [result, setResult] = useState()
    const isLoading = false

    const handleInputChange = () => {

    }

    const handleSubmit = () => {

    }

    return (
        <div className="pharmacy-card">
          <h1>Online Pharmacy</h1>
          <div className="form-container">
            <div className="form-group">
              <label htmlFor="ssn">Social Security Number</label>
              <input
                type="text"
                id="ssn"
                value={data.ssn}
                onChange={handleInputChange}
              />
            </div>
            
            <div className="form-group">
              <label htmlFor="fname">First Name</label>
              <input
                type="text"
                id="fname"
                value={data.fname}
                onChange={handleInputChange}
              />
            </div>
            
            <div className="form-group">
              <label htmlFor="lname">Last Name</label>
              <input
                type="text"
                id="lname"
                value={data.lname}
                onChange={handleInputChange}
              />
            </div>
            
            <div className="form-group">
              <label htmlFor="med">Medication</label>
              <input
                type="text"
                id="med"
                value={data.med}
                onChange={handleInputChange}
              />
            </div>
            
            <div className="form-group">
              <label htmlFor="dos">Dosage</label>
              <input
                type="text"
                id="dos"
                value={data.dos}
                onChange={handleInputChange}
              />
            </div>
    
            <button 
              onClick={handleSubmit}
              disabled={isLoading}
              className={`submit-button ${isLoading ? 'loading' : ''}`}
            >
              {isLoading ? 'Submitting...' : 'Submit'}
            </button>
    
            <textarea
              value={result}
              readOnly
              className="result-textarea"
              rows={3}
            />
          </div>
        </div>
      );
}

export default PharmacyForm