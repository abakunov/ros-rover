import React from 'react';
import './App.css';
import { ChoosePortModal } from './components/choose-port-modal';
import { NavBar } from './components/navbar';

enum ActivePage {
  Settings,
  Modal,
  Panel
}

interface AppState{
  activePage : ActivePage,
  port : String,
}

class App extends React.Component<{},AppState>{

  constructor(props : AppState) {
    super(props);
    this.state = {
      activePage : ActivePage.Modal,
      port : ""
    };
  }

  toggleClickHandler = () : void =>{
    return
  }

  choosePort = (newPort:string):void=>{
    this.setState({
      port : newPort,
      activePage : ActivePage.Panel
    });
  }

  public render(){
    return (
      <div>
        
        <NavBar gotoSettings = {this.toggleClickHandler} commandsInQueue = {3}></NavBar>

        {
          this.state.activePage == ActivePage.Modal ? <ChoosePortModal choosePort = {this.choosePort}></ChoosePortModal>:
          <div></div>
        }

        
      </div>
    )
  }
}

export default App;
