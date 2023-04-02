import React from "react";
// import InputField from "./InputField";
import SubmitButton from "./SubmitButton";


class LoginForm extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            password : ''
        }
    }

    handlePasswordChange = (e) => {
        this.setState({
            password : e.target.value
        })
    }

    render() {
        return (
            <div className="loginForm">
                Log In
                <label htmlFor="username">Username</label> 
                <input name="username" id="username" type='text' placeholder='Username' value={this.props.username ? this.props.username : ''} onChange={this.props.handleLoginChange} />
                <label htmlFor="password">Password</label>
                <input name="password" id="password" type='password' placeholder='Password' value={this.state.password ? this.state.password : ''} onChange={this.handlePasswordChange} />
                <SubmitButton text='Login' disabled={this.state.buttonDisabled} onClick={ e => this.props.handleLogin(e, {
                    username : this.props.username, 
                    password : this.state.password
                })} />
            </div>
        )
    }
}

export default LoginForm;


// constructor(props){
//     super(props);
//     this.state = {
//         username: '',
//         password: '',
//         buttonDisabled: false
//     }
// }

// setInputValue(property, val) {
//     val = val.trim();
//     this.setState({
//         [property]: val
//     })
// }

// resetForm() {
//     this.setState({
//         username: '',
//         password: '',
//         buttonDisabled:false
//     })
// }

// async doLogin() {
//     if(!this.state.username) {
//         return;
//     }
//     if(!this.state.password){
//         return;
//     }
//     this.setState({
//         buttonDisabled:true
//     })
    
//     try{
//         let res = await fetch('/login', {
//             method: 'post',
//             headers: {
//                 'Accept': 'application/json',
//                 'Content-Type': 'application/json'
//             },
//             body: JSON.stringify({
//                 username: this.state.username,
//                 password: this.state.password
//             })
//         });

//         let result = await res.json();
//         if(result && result.success) {
//             UserStore.isLoggedIn = true;
//             UserStore.username = result.username;
//         }
//         else if(result && result.success == false){
//             this.resetForm();
//             alert(result.msg);
//         }
//     }
//     catch(e) {
//         console.log(e);
//         this.resetForm();
//     }
// }

{/* <div className="loginForm">
                Log In 
                <InputField type='text' placeholder='Username' value={this.state.username ? this.state.username : ''} onChange={ (val) => this.setInputValue('username', val)} />
                <InputField type='password' placeholder='Password' value={this.state.password ? this.state.password : ''} onChange={ (val) => this.setInputValue('password', val)} />
                <SubmitButton text='Login' disabled={this.state.buttonDisabled} onClick={ () => this.doLogin() } />
            </div> */}