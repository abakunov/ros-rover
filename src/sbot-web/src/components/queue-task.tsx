import React from 'react';
import '../css/main.css';
import '../css/pallete.css';
import { TaskStatus } from '../enums/taskStatus';

interface QueueTaskProps {
    commandName : string,
    status: TaskStatus
}

interface QueueTaskState{
    status: TaskStatus
}

export class QueueTask extends React.Component<QueueTaskProps,QueueTaskState> {

    constructor(props : QueueTaskProps) {
        super(props);
        this.state = {
          status: props.status
        };
      }

    render() {
        return (
            <div className="">
                <div className="queue-lest-command">
                    <div className="queue-lest-command-header">
                        {this.props.commandName}
                    </div>
                    <div className="queue-lest-command-status">
                        {this.state.status}
                    </div>
                </div>
                <div className="queue-lest-command-buttons">
                    Убрать комманду
                </div>
            </div>
        )
    }
}