import React from 'react';
import InputField from '../InputField';
import SubmitButton from '../SubmitButton';
import UserStore from '../stores/UserStore';


class LoginForm extends React.Component {


  constructor(props) {
    super(props);
    this.state = {
      username: '', //string
      password: '',  //string
      buttonDisabled: false //used when user clicks log in and the API checks if the user Exists
    }
  }

  setInputValue(property, val) {
    val = val.trim(); {
      if (val.length > 12) {  //setting max length of both username and password to 12
        return;
      }
      this.setState({
        [property]: val
      })

    }
  }

  resetForm() { //reset form if form is incorrect - eg, if user type wrong password or wrong username
    this.setState({
      username: '',
      password: '',
      buttonDisabled: false
    })
  }

  async doLogin() { //Call a new api call
    //this will be called later when we click submit button to log in

    if (!this.state.username) {
      return;
    }

    if (this.state.password) {
      return;
    }

    this.state({
      buttonDisabled: true

    })

    try {

      // access API point
      let res = await fetch('/login', {
        method: 'post',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          // this will send the password and username to the API
          //and check the database if the password and username exists
          // and then create a session and log in user
          username: this.state.username,
          password: this.state.password
        })
      });


      let result = await res.json();
      if (result && result.success) {
        //if user successfully logged in
        UserStore.isLoggedIn = true;
        UserStore.username = result.username;
      }

      else if (result && result.success === false) {
        this.resetForm();
        alert(result.msg); // Alert the error, so we can create a property from message and return the message from API later

      }

    }
    catch (e) {
      console.log(e);
      this.resetForm(); // so can reset the form

    }



  }

  render() {
    return (
      <div className="loginForm">
        Log In to the Bank
        <InputField
          type='text'
          placeholder='Username'
          value={this.state.username ? this.state.username : ''}
          //validationSchema= string().required('Username is required') 
          onChange={(val) => this.setInputValue('username', val)}
        />

        <InputField
          type='password'
          placeholder='Password'
          value={this.state.password ? this.state.password : ''}
          onChange={(val) => this.setInputValue('password', val)}
        />

        <SubmitButton

          text='Login'
          disable={this.state.buttonDisabled}
          onClick={() => this.doLogin()} //call to the API

        />







      </div>
    );
  }
}

export default LoginForm;
