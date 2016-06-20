//
//  ViewController.swift
//  PythonToSwiftExample
//
//  Created by Nicholas Devenish on 17/06/2016.
//  Copyright © 2016 Nicholas Devenish. All rights reserved.
//

import Cocoa

class ViewController: NSViewController {

  override func viewDidLoad() {
    super.viewDidLoad()
    let pythonMessage = Bridge.sharedInstance().getPythonInformation()
    Swift.print("Info from python:\n\(pythonMessage)")
    
    // Do any additional setup after loading the view.
  }

  override var representedObject: AnyObject? {
    didSet {
    // Update the view, if already loaded.
    }
  }


}

