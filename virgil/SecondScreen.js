import React from 'react';
import {Text, View, Button} from 'react-native';
const util = require('util');

export default class SecondScreen extends React.Component {
    static navigationOptions = {
        title: 'Second Screen'
    };
    render() {
        var {params} = this.props.navigation.state;

        return(
            <View>
                <Text>This is screen 2</Text>
                <Text> Params from screen1 : {params.name}, email = {params.email}</Text>
            </View>
        )
    }
}