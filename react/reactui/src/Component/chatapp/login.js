import React, { Component } from 'react'
import "./login.css" 

export class login extends Component {
    render() {
        return (
            <div className= "login">
            <table className="table">
                <h1>Login </h1>
            <tr> 
                <td>Username</td>
                <td><input type='text' className="input"></input></td>
            </tr>
            <tr>
                <td> Enter password</td>
                <td><input type='password' className='input' ></input></td>
            </tr>
            <tr>
               <td colSpan="2" ><button type='submit' className= 'Button'>Login!</button></td>
            </tr>
            </table>
            </div>
        )
    }
}

export default login
