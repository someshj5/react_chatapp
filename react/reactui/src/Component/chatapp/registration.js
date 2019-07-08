import React, { Component } from 'react'
import "./registration.css" 

export class registration extends Component {
    render() {
        return (
            <div className= "registration">
            <table className="table">
                <h1>Registration </h1>
            <tr> 
            <td>Firstname</td>
            <td><input type='text' className="input"></input></td>
            </tr>
            <tr>
                <td>Lastname</td>
                <td><input type= 'text' className='input'></input></td>
            </tr>
            <tr>
            <td> Create password</td>
            <td><input type='password' className='input' ></input></td>
            </tr>
           <tr>
               <td>Confirm password</td>
               <td><input type='password' className='input'></input></td>

           </tr>
           <tr>
               <td colSpan="2" ><button type='submit' className= 'Button'>Signup</button></td>
           </tr>

            </table>
                
            </div>
        )
    }
}

export default registration
