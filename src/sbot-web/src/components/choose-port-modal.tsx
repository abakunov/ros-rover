import React from 'react';
import '../css/modal.css';
import '../css/main.css';

interface choosePortModalState {
    ports: Array<String>;
    port : string;
}

interface choosePortModalProps {
    choosePort: (arg0 : string) => void;
    apply : any;
}


export class ChoosePortModal extends React.Component<choosePortModalProps, choosePortModalState> {

    constructor(props: choosePortModalProps) {
        super(props);
        this.state = { ports: [], port:"" };
        this.change = this.change.bind(this);
        this.changeGlobal = this.changeGlobal.bind(this);
    }

    async getPorts()  {
        let url = 'http://0.0.0.0:5000/get_serial_ports';
        let response = await fetch(url);
        let response_json = await response.json();
     
        console.log(response_json['ports']);
        
        this.setState({
            ports: response_json['ports']
        });

        if (response_json['ports'].length>0){
            
           this.setState({
            port : response_json['ports'][0]
           });
           this.props.choosePort(this.state.port);
           
           
        }
    }
    change(event: any ) {
        this.setState({
            port : event.target.value
        });
        this.props.choosePort(event.target.value);
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
                    <div className="modal-apply-button" onClick = {(event)=>this.props.apply(event)}>
                        Apply
                    </div>
                </div>
            </div>
        )
    }
}