import { Command } from "./Command";

export interface Queue{
    data : Array<Command>;
    active : Command;
}
