//
//  ViewController.swift
//  HackSprint
//
//  Created by Katie Cai on 2/14/18.
//  Copyright © 2018 Katie Cai. All rights reserved.
//

import UIKit
import GoogleMaps
import GooglePlaces
import Alamofire
import Foundation

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    override func loadView() {
        let camera = GMSCameraPosition.camera(withLatitude: 34.0689, longitude: -118.4452, zoom: 15.0)
        let mapView = GMSMapView.map(withFrame: CGRect.zero, camera: camera)
        view = mapView
        
        let marker = GMSMarker()
        marker.position = CLLocationCoordinate2D(latitude: 34.0689, longitude: -118.4452)
        marker.title = "UCLA"
        marker.map = mapView
        
        getClasses(building: "Broad Art Center");
    }
    
    func getClasses(building: String) {

        Alamofire.request("http://api.ucladevx.com/courses/Winter/all").responseJSON { (response) in
            
            guard response.result.isSuccess else {
                print("HUGGEEE Error getting shit")
                return
            }
            
            var filteredClasses: [uclass] = []
            print(type(of:response.data))
            let json = try? JSONSerialization.jsonObject(with: response.data!, options: [])
            if let j = json! as? [Any] {
                for anyC in j {
                    if let c = anyC as? [String: String] {
                        let course = c["course"]
                        let subject = c["subject"]
                        
                        let instructors = c["instructors"]
                        let locations = c["locations"]
                        let day_times = c["day_times"]
                        var location = locations?.components(separatedBy: "|*|")
                        var instructor = instructors?.components(separatedBy: "|*|")
                        var day_time = day_times?.components(separatedBy: "|*|")
                        for (i, loc) in location!.enumerated() {
                            if (loc.range(of:building) != nil) {
                                let myClass = uclass(course: course!, subject: subject!, location: loc, instructor: instructor![i], day_time: day_time![i])
                                filteredClasses.append(myClass)
                            }
                        }
                    }
                }
            }
            print(filteredClasses)
//            print(buildings)
            
//            print(String(data: response.data!, encoding: String.Encoding.utf8)!)
        }
    }

}

