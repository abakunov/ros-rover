import React from 'react';
import './App.css';
import { ChoosePortModal } from './components/choose-port-modal';
import { Pallete } from './components/command-pallete';
import { NavBar } from './components/navbar';

enum ActivePage {
  Settings,
  Modal,
  Panel
}

interface AppState {
  activePage: ActivePage,
  port: string,
}

class App extends React.Component<{}, AppState>{

  constructor(props: AppState) {
    super(props);
    this.state = {
      activePage: ActivePage.Modal,
      port: ""
    };

    this.navigateToMain = this.navigateToMain.bind(this);
  }

  toggleClickHandler = (): void => {
    return
  }

  choosePort = (newPort: string): void => {
    this.setState({
      port: newPort,
    });
  }

  navigateToMain = (event: any): void => {
    const data = { port: this.state.port };
    console.log(data);
    
    //POST request with body equal on data in JSON format
    fetch('http://0.0.0.0:5000/set_serial_port', {
      method: 'POST',
      body: JSON.stringify(data),
    })


    this.setState({
      activePage: ActivePage.Panel,
    });
  }

  public render() {
    return (
      <div>

        <NavBar gotoSettings={this.toggleClickHandler} commandsInQueue={3}></NavBar>

        {
          this.state.activePage == ActivePage.Modal ? <ChoosePortModal apply={this.navigateToMain} choosePort={this.choosePort}></ChoosePortModal> :
            <Pallete port={this.state.port} />
        }


      </div>
    )
  }
}

export default App;
