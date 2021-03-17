import React from 'react';
import '../css/main.css';
import '../css/pallete.css';
import { TaskStatus } from '../enums/taskStatus';
import { Queue } from '../models/Queue';
import { QueueTask } from './queue-task';
import {Task} from '../models/Task';
import Modal from 'react-modal';
import { Command } from '../interfaces/Command';
import AviableCommands from '../aviableCommands';
import { Command2Send } from '../models/Command2Send';
import { CommandToSend } from './taskToSend';

interface PalleteState{
    port : string;
    queue : Queue;
    openedModal : boolean;
    commandsToSend : Array<Command2Send>;
}

interface PalleteProps{
    port : string;
}
const customStyles = {
    content : {
      top                   : '50%',
      left                  : '50%',
      right                 : 'auto',
      width                 : '50%',
      height                : '50%',
      bottom                : 'auto',
      marginRight           : '-50%',
      borderRadius          : '30px',
      transform             : 'translate(-50%, -50%)'
    }
  };

export class Pallete extends React.Component<PalleteProps , PalleteState> {

    constructor(props : PalleteProps) {
        super(props);
        this.state = {
            port : props.port,
            queue : new Queue([]),
            openedModal : false,
            commandsToSend : []
        };
        this.openModal = this.openModal.bind(this);
        this.closeModal = this.closeModal.bind(this);
        this.change = this.change.bind(this);
        this.addCommand2Send = this.addCommand2Send.bind(this);
        
    }

    componentDidMount(){
        this.state.queue.fromJson(
            '{"tasks" : [{"name" : "test","status" : "","propName":"speed","propValue":"1000"}]}'
        );
        this.setState({
            queue : this.state.queue
        })
    }

    closeModal(){
        this.setState({openedModal:false});
    }

    openModal(){
        this.setState({openedModal:true});
    }

    change(){
        
    }

    addCommand2Send(){
        this.state.commandsToSend.push(new Command2Send(AviableCommands[0]));
        this.setState({commandsToSend: this.state.commandsToSend});
    }

    render(){
        return(
        <div className="container">
            <Modal
            isOpen={this.state.openedModal}
      
            onRequestClose={this.closeModal}
            style={customStyles}
            contentLabel="Send Command"
            >
            <div className="send-modal">
                <div className="send-modal-header">
                    Отослать новые команды
                </div>
                {this.state.commandsToSend.map((command,i) => <CommandToSend></CommandToSend>)}
                <div className="add-command-to-send" onClick={this.addCommand2Send}>
                    +
                </div>
            </div>
            </Modal>
            <div className="pallete-main">
                <div className="queue-list">
                    <div className="queue-list-header">
                        Очередь комманд:    
                    </div>
                    <div className="clear-queue">
                        Очистить очередь
                    </div>
                    <div className="queue-list-queue">
                        {this.state.queue.data.map((task : Task) => 
                            <QueueTask commandName = {task.name} status = {task.status}></QueueTask>
                        )}
                    </div>
                </div>
                <div className="flex-2">

                </div>
                <div className="send-command">
                    <div className="queue-list-header">
                        Отослать комманду:    
                    </div>
                    <div className="commads-list">
                        <div className="button-blue cmd-btn" onClick={this.openModal}>
                            Вперед
                        </div>
                        <div className="button-blue cmd-btn">
                            Назад
                        </div>
                        <div className="button-blue cmd-btn">
                            Поворот
                        </div>
                    </div>
                </div>
            </div>
            
        </div>
        )
    }

}