import React from 'react';
import {Text, View, Button} from 'react-native';
const util = require('util');

export default class SecondScreen extends React.Component {
    static navigationOptions = {
        title: 'Virgil'
    };
    render() {
        var {params} = this.props.navigation.state;
        var {navigate} = this.props.navigation;
        return(
            <View>
                <Text>Choose your language. </Text>
                <Button 
                    onPress = {
                        () => navigate("Camera", {name: "tanzeela", email: "tanz@gmail.com"})
                    }
                    title = "Enter"
                />
                <Text>English (default) </Text>
            </View>
        )
    }
}