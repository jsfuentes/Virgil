import React from 'react';
import {Text, View} from 'react-native';

import { StackNavigator } from 'react-navigation';
import HomeScreen from './screens/HomeScreen';
import OptionScreen from './screens/OptionScreen';
import CameraScreen from './screens/CameraScreen';

const Navigation = StackNavigator({
    Home: {screen: HomeScreen},
    Options: {screen: OptionScreen},
    Camera: {screen: CameraScreen}
});
export default Navigation;