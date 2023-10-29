//
//  MainView.swift
//  start_code
//
//  Created by Kristian Sæberg on 28/10/2023.
//

import SwiftUI

struct MainView: View {
    @Binding var tabSelection: Int

    var body: some View {
        NavigationView{
            ZStack{
                Image("pizza") // Assuming "pizza" is the name of the image asset in Assets.xcassets
                    .resizable()
                    .aspectRatio(contentMode: .fill)
                    .cornerRadius(100) // Adjust the corner radius as needed
                    .frame(maxWidth: 400, maxHeight: 800)
                    .clipped()
                    .offset(y: -60)
                VStack{
                    Text("Hei! La oss bekjempe matsvinn sammen!")
                        .frame(maxWidth: 350, maxHeight:300)
                        .shadow(color: .black, radius: 5)
                        .foregroundColor(.white)
                        .font(.system(size: 50, weight: .bold, design: .rounded))
                    Button() {
                        self.tabSelection = 4
                    }label: {
                        Text("Finn oppskrifter")
                            .font(.system(size: 25, weight: .bold, design: .rounded))
                            .foregroundColor(.white)
                            .frame(width: 300, height: 50)  
                            .background(
                                RoundedRectangle(cornerRadius: 15, style: .continuous)
                                    .fill(.red)
                            )
                    }
                }
                
            }
        }
    }
}

struct MainView_Previews: PreviewProvider {
    static var previews: some View {
        MainView(tabSelection: .constant(1))
    }
}
