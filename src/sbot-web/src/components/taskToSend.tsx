import React from 'react';
import AviableCommands from '../aviableCommands';
import '../css/main.css';
import '../css/pallete.css';
import { Command2Send } from '../models/Command2Send';

interface CommandToSendProps {
    index : number;
    change : any;
    del : any;
    updateVal:any;
    command : Command2Send;
}

interface CommandToSendState {

}

export class CommandToSend extends React.Component<CommandToSendProps, CommandToSendState> {
    
    constructor(props: CommandToSendProps) {
        super(props);
    }
    public render() {
        return (
            <div >

                <select onChange={(event)=>this.props.change(event,this.props.index)} className="modal-selected-port">
                    {AviableCommands.map((cmd, i) => {
                        return (<option value={i}>{cmd.title}</option>)
                    })}
                </select>
                <div className="param-add">
                    <div className="t2s-param">
                        {this.props.command.command.propName}
                    </div>
                    <input value={this.props.command.command.propValue} className="t2s-value" onChange={(event)=>this.props.updateVal(this.props.index, event)} ></input>
                </div>
                <div className="button-red-modal" onClick={()=>this.props.del(this.props.index)}>
                    Удалить
                </div>

            </div>
        )
    }
}