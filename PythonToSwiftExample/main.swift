// Application main entry point


import Cocoa

let path = Bundle.main().pathForResource("Bridge", ofType: "plugin")
guard let pluginbundle = Bundle(path: path!) else {
  fatalError("Could not load python plugin bundle")
}
pluginbundle.load()

NSApplicationMain(Process.argc, Process.unsafeArgv)

