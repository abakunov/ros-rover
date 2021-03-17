import React from 'react';
import '../css/modal.css';
import '../css/main.css';

interface choosePortModalState {
    ports: Array<String>;
    port : string;
}

interface choosePortModalProps {
    choosePort: (arg0 : string) => void;
}


export class ChoosePortModal extends React.Component<choosePortModalProps, choosePortModalState> {

    constructor(props: choosePortModalProps) {
        super(props);
        this.state = { ports: [], port:"" };
        this.change = this.change.bind(this);
        this.changeGlobal = this.changeGlobal.bind(this);
    }

    getPorts() {
        this.setState({
            ports: ["test/1", "test/2"]
        });
    }
    change(event: any ) {
        this.setState({
            port : event.target.value
        });
    }

    changeGlobal(event : any){
        this.props.choosePort(this.state.port);
    }

    componentDidMount() {
        this.getPorts();
    }

    public render() {
        return (
            <div className="modal-container">
                <div className="modal">
                    <div className="modal-header">
                        Выберите порт, к которому подключен приемник:
                    </div>
                    <select onChange = {this.change} className="modal-selected-port">
                        {this.state.ports.map((port, i) => {
                            return (<option>{port}</option>)
                        })}
                    </select>
                    <div className="modal-apply-button" onClick = {this.changeGlobal}>
                        Apply
                    </div>
                </div>
            </div>
        )
    }
}