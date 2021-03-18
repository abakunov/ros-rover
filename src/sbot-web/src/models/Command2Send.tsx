import { Command } from "../interfaces/Command";

export class Command2Send {

    command: Command;
  
    constructor(command: Command) {
      this.command = command;
    }
  
    send(){
      const data = { command: this.command.command , value: this.command.propValue};
      console.log(data);
      
      //POST request with body equal on data in JSON format
      fetch('http://0.0.0.0:5000/execute_command', {
        method: 'POST',
        body: JSON.stringify(data),
      })
    }
  
  
    }