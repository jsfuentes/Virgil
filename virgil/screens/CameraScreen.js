import React from 'react';
import {Text, View, Button} from 'react-native';
const util = require('util');

export default class SecondScreen extends React.Component {
    static navigationOptions = {
        title: 'Virgil'
    };
    render() {
        var {params} = this.props.navigation.state;
        return(
            <View>
                <Text>Camera here </Text>
            </View>
        )
    }
}