import React from 'react';
import {Text, View} from 'react-native';

import { StackNavigator } from 'react-navigation';
import HomeScreen from './HomeScreen';
import OptionScreen from './OptionScreen';
import CameraScreen from './CameraScreen';

const Navigation = StackNavigator({
    Home: {screen: HomeScreen},
    Options: {screen: OptionScreen},
    Camera: {screen: CameraScreen}
});
export default Navigation;