//
//  MainView.swift
//  start_code
//
//  Created by Kristian Sæberg on 28/10/2023.
//

import SwiftUI

struct ContentView: View {
    @State private var tabSelection = 1
    @State private var updateValue = UUID()


    var body: some View {
        TabView(selection: $tabSelection) {
            MainView(tabSelection: $tabSelection)
                .tabItem {
                    Label("", systemImage: "house.fill")
                }
                .tag(1)

            IngredientsView()
                .tabItem {
                    Label("", systemImage: "cabinet")
                }
                .tag(2)

            ShoppingCartView()
                .tabItem {
                    Label("", systemImage: "basket")
                }
                .onAppear {
                    // Subscribe to the notification
                    NotificationCenter.default.addObserver(forName: UIApplication.willEnterForegroundNotification, object: nil, queue: .main) { _ in
                        // Update the state to trigger a view update
                        self.updateValue = UUID()
                    }
                }
                .tag(3)

            SuggestedRecepiesView()
                .tabItem {
                    Label("", systemImage: "book")
                }
                .tag(4)
        }
        .onAppear(){
            UITabBar.appearance().backgroundColor = .white
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        MainView(tabSelection: .constant(1))
    }
}
