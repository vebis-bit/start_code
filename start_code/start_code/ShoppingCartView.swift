//
//  ShoppingCartView.swift
//  start_code
//
//  Created by Kristian Sæberg on 29/10/2023.
//

import SwiftUI

struct cart: Decodable {
    let cart: [String:Float]
}

struct ShoppingCartView: View {
    @State private var ShoppinCart: cart?

    var body: some View {
        VStack {
            if let data = ShoppinCart {
                List {
                    Text("Handlekurv")
                        .shadow(color: .black, radius: 5)
                        .frame(maxWidth: 350, maxHeight:300)
                        .foregroundColor(.white)
                        .font(.system(size: 50, weight: .bold, design: .rounded))
                        .listRowBackground(
                            RoundedRectangle(cornerRadius: 5)
                                .fill(.clear)
                        )
                    Section() {
                        ForEach(Array(data.cart), id: \.key) { key, value in
                            HStack{
                                Text(String(key))
                                Spacer()
                                Text("\(String(value)) g")
                            }
                        }
                        .listRowBackground(
                            RoundedRectangle(cornerRadius: 5)
                                .fill(Color.white)
                                .padding(2)
                        )
                        .listRowSeparator(.hidden)
                    }
                }
                .background(Image("handleliste")
                    .resizable()
                    .scaledToFill()
                    .ignoresSafeArea()
                )
                .scrollContentBackground(.hidden)
            } else {
                Text("Laster inn handlekurv...")
            }
        }
        .onAppear {
            fetchData()
        }
    }
    
    func fetchData() {
        guard let url = URL(string: "http://127.0.0.1:8000/shoppingcart") else { return }
        
        URLSession.shared.dataTask(with: url) { data, _, _ in
            guard let data = data else { return }
            
            do {
                let decodedData = try JSONDecoder().decode(cart.self, from: data)
                DispatchQueue.main.async {
                    self.ShoppinCart = decodedData
                }
            } catch {
                print("Error decoding: \(error)")
            }
        }.resume()
    }
}

struct ShoppingCartView_Previews: PreviewProvider {
    static var previews: some View {
        ShoppingCartView()
    }
}
