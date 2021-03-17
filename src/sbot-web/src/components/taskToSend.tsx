import React from 'react';
import AviableCommands from '../aviableCommands';
import '../css/main.css';
import '../css/pallete.css';

interface CommandToSendProps {

}

interface CommandToSendState {

}

export class CommandToSend extends React.Component<CommandToSendProps, CommandToSendState> {
    change() { }
    public render() {
        return (
            <div >
                <select onChange={this.change} className="modal-selected-port">
                    {AviableCommands.map((cmd, i) => {
                        return (<option>{cmd.title}</option>)
                    })}
                </select>
            </div>
        )
    }
}