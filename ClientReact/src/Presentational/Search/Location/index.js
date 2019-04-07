import React from 'react'

const Location = ({location, handleChange, handleSubmit}) =>
    <div className='Location'>
        <h2> Search Location Details </h2> <br />
        <form onSubmit={handleSubmit}>
         <label>
           Country <br />
           <select onChange={handleChange('Country')}>
                <option selected disabled hidden> Select Country </option>
                <option value="United States"> United States </option>
           </select> <br />
           State <br />
           <select onChange={handleChange('State')}>
                <option selected disabled hidden> Select State</option>
                <option value="California"> California </option>
                <option value="Texas"> Texas </option>
             <  option value="North Carolina"> North Carolina </option>
           </select> <br />
           City <br />
           <select  onChange={handleChange('City')}>
                <option selected disabled hidden> Select City </option>
                <option value="Anaheim"> Anaheim </option>
                <option value="Huntington Beach"> Huntington Beach </option>
                <option value="Irvine"> Irvine </option>
           </select> <br />
         </label>
         <input type="submit" value="Submit" />
        </form>
    </div>;

export default Location;


