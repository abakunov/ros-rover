export class Command {

  command: string;
  title: string;
  propName : string;
  propValue : string;

  constructor(command: string, title : string, propName:string,propValue : string) {
    this.command = command;
    this.propName = propName;
    this.title = title;
    this.propValue = propValue;
  }



  }