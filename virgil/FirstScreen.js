import React from 'react';
import {Text, View, Button} from 'react-native';
const util = require('util');

export default class FirstScreen extends React.Component {
    static navigationOptions = {
        title: 'First Screen'
    };
    
    render() {
        var {navigate} = this.props.navigation;
        return(
            <View>
                <Text>This is screen 1</Text>
                <Button 
                    onPress = {
                        () => navigate("Second", {name: "tanzeela", email: "tanz@gmail.com"})
                    }
                    title = "Go to Screen 2"
                />
            </View>
        )
    }
}