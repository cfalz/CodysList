import React from 'react'


const DropDown = ({title, options, handleChange, handleSubmit}) =>
    <form onSubmit={handleSubmit}>
        <div className={title}>
            <h2> {title} </h2> <br />
            {options.map((option) => console.log('id: ' + option.id + ' title: ' + option.title + ' content: ' + option.content))}
                {options.map((option) =>
                    <div className={option.id}>
                       <label> {option.title} </label>
                       <br />
                       <select defaultValue={option.selected_default} onChange={handleChange(option.title)}>
                            {option.content.map((option) => <option value={option.value}> {option.value} </option>)}
                       </select>
                       <br />
                    </div>
                 )}
             <input type="submit" value="Submit" />
        </div>
    </form>;

export default DropDown;


