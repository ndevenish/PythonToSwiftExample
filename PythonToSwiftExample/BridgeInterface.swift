//  BridgeInterface.swift

import Foundation

/// A simple demonstration interface to the python module
@objc public protocol BridgeInterface {
  static func createInstance() -> BridgeInterface
  func getPythonInformation() -> String
}

/// A simple class for access to an instance of the python interface
class Bridge {
  static private var instance : BridgeInterface?
  
  static func sharedInstance() -> BridgeInterface {
    return instance!
  }
  static func setSharedInstance(to: BridgeInterface?) {
    instance = to
  }
}
