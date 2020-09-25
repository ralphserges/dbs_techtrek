import React from 'react';
import { observer } from 'mobx-react';
import UserStore from './stores/UserStore';
import LoginForm from './Login/LoginForm';
import InputField from './InputField';
import SubmitButton from './SubmitButton';

import './App.css';

class App extends React.Component {

  async componentDidMount() {
    try {

      let res = await fetch('/isLoggedIn', {
        method: 'post',
        headers: {
          'Accept': 'application/json',
          'Content-type': 'application/json'
        }
      });

      let result = await res.json();
      if (result && result.success) {
        UserStore.loading = false;
        UserStore.isLoggedIn = true;
        UserStore.username = result.username;
      }
      else {
        UserStore.loading = false;
        UserStore.isLoggedIn = false;
      }
    }

    catch (e) {
      UserStore.loading = false;
      UserStore.isLoggedIn = false;
    }
  }

  // //upon logging out
  // async doLogOut() {
  //   try {

  //     let res = await fetch('/logout', {
  //       method: 'post',
  //       headers: {
  //         'Accept': 'application/json',
  //         'Content-Type': 'appliocation/json'
  //       }
  //     });

  //     let result = await res.json();
  //     if (result && result.success) {
  //       UserStore.isLoggedIn = false; //MEANS  user has logged out
  //       UserStore.username = ''; //then Reset username is the userstore
  //     }

  //   }
  //   catch (e) {
  //     console.log(e);

  //   }
  // }

  render() {
    //If app is loading, return some HTML
    if (UserStore.loading) {
      return (
        <div className="app">
          <div className='container'>
            Loading, pls wait....
            </div>
        </div>
      );
    }
    else {
      if (UserStore.isLoggedIn) {
        return (
          <div className="app">
            <div className='container'>
              Welcome {UserStore.username} back,
              <SubmitButton
                text={'log out'}
                disabled={false}
                onClick={() => this.doLogOut()}
              />

            </div>
          </div>
        );
      }



      //if not logged in this is what we return
      return (
        <div className="app" >
          <div className='container'>
           
            <LoginForm />

          </div>
        </div>
      );
    }
  }
}



export default observer(App);
