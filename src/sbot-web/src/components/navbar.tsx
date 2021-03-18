import React from 'react';
import '../css/navbar.css';
import '../css/main.css';

interface NavBarProps{
    gotoSettings : () => void;
    commandsInQueue : number;
}

interface NavBarState{

}

export class NavBar extends React.Component<NavBarProps, NavBarState> {
    public render(){
        return (
            <div className="nav-wr">
                <div className="container">
                      <div className="nav">
                        <div className="nav-header flex-7">
                            S+ command palette
                        </div>
                        <div className="nav-right-menu flex-7">
                            <div className="queue-status">
                                {this.props.commandsInQueue} tasks in queue
                            </div>
                            <div className="button-blue ">
                                settings
                            </div>
                        </div>  

                    </div>
                </div>
            </div>
        )
    }
}