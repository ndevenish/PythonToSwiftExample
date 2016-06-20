// Application main entry point


import Cocoa

// Load the python-based plugin bundle
let path = Bundle.main().pathForResource("Bridge", ofType: "plugin")
guard let pluginbundle = Bundle(path: path!) else {
  fatalError("Could not load python plugin bundle")
}
pluginbundle.load()

// Load the principal class
guard let pc = pluginbundle.principalClass as? BridgeInterface.Type else {
  fatalError("Could not load principal class from python bundle")
}

// Create an instance of the principal class and store it
let interface = pc.createInstance()
Bridge.setSharedInstance(to: interface)

NSApplicationMain(Process.argc, Process.unsafeArgv)

