import React from 'react';
import {Text, View} from 'react-native';

import { StackNavigator } from 'react-navigation';
import FirstScreen from './FirstScreen';
import SecondScreen from './SecondScreen';

const Navigation = StackNavigator({
    First: {screen: FirstScreen},
    Second: {screen: SecondScreen}
});
export default Navigation;