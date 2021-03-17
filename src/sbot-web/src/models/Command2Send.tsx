import { Command } from "../interfaces/Command";

export class Command2Send {

    command: Command;
  
    constructor(command: Command) {
      this.command = command;
    }
  
    send(){
      console.log("Command sent");
    }
  
  
    }