import React from 'react';
import {Text, View, Button} from 'react-native';
const util = require('util');

export default class FirstScreen extends React.Component {
    static navigationOptions = {
        title: 'Virgil'
    };
    
    render() {
        var {navigate} = this.props.navigation;
        return(
            <View>
                <Text>Virgil</Text>
                <Button 
                    onPress = {
                        () => navigate("Options", {})
                    }
                    title = "Enter"
                />
            </View>
        )
    }
}