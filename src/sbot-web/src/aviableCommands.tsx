import { Command } from "./interfaces/Command";

var AviableCommands = [
    new Command("64","Вперед", "Расстояние(см)","100"),
    new Command("cc","Установить лин. скорость", "Скорость(см/cек)","40"),
    new Command("00", "Очистить очередь", "Любое","0"),
    new Command("10" , "Включить LED","Любое","0"),
    new Command("11", "Выключить LED","Любое","0"),
    new Command("aa", "Установить угл. скорость", "Скорость(n сотых рад/cек)","100"),
    new Command("bb" , "Назад", "Расстояние(см)","100"),
    new Command("03" ,"Поворот влево", "угол(град)", "90"),
    new Command("04" ,"Поворот направо", "угол(град)", "90"),
    new Command("05" ,"Поворот горизонт. серво", "угол(град)", "90"),
    new Command("06" ,"Поворот верт. серво", "угол(град)", "90"),

];

export default AviableCommands;