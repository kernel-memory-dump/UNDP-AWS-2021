import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Tour of Heroes';

  someMethod() {
    const x = 2;

    const z = 5;

    const y = 3;
    return x + y + z;
  }
}
