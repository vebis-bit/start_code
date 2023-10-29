//
//  SuggestedView.swift
//  start_code
//
//  Created by Kristian Sæberg on 28/10/2023.
//

import SwiftUI

struct namesData: Decodable {
    let name: [String: String]
}

struct SuggestedView: View {
    @State private var selectedItem: String?
    @State private var isRecepiePresented = false
    @State private var fetchedNames: namesData?

    var body: some View {
        NavigationView{
            if let data = fetchedNames{
                List {
                    ForEach(Array(data.name), id: \.key) { key, value in
                        HStack{
                            Text("tiss")
                            Text(value)
                            Button {
                                isRecepiePresented.toggle()
                            } label: {
                                Text("Gå til oppskrift")
                            }
                            .sheet(isPresented: $isRecepiePresented) {
                                RecepieView(selectedItem: "tass")
                            }
                        }
                    }
                }
                .navigationTitle("Dette kan du lage")
            }
        }
        .onAppear {
            fetchNamesData()
        }
    }
    
    func fetchNamesData() {
        guard let url = URL(string: "http://127.0.0.1:8000/ablerecepiesNames") else { return }

        URLSession.shared.dataTask(with: url) { data, _, _ in
            guard let data = data else { return }
            print(data.base64EncodedString())
            do {
                let decodedData = try JSONDecoder().decode(namesData.self, from: data)
                DispatchQueue.main.async {
                    self.fetchedNames = decodedData
                    print(decodedData)
                }
            } catch {
                print("Error decoding: \(error)")
            }
        }.resume()
    }
}


