/*
 * Copyright 2014 Effektif GmbH.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package com.effektif.email;

import java.util.ArrayList;
import java.util.List;


/** service for testing that stores the sent emails in a list 
 * instead of sending them.
 * 
 * @author Tom Baeyens
 */
public class TestOutgoingEmailService implements OutgoingEmailService {
  
  public List<OutgoingEmail> emails;

  @Override
  public void send(OutgoingEmail email) {
    emails.add(email);
  }
  
  public void reset() {
    emails = new ArrayList<>();
  }

  @Override
  public String validate(String emailAddress) {
    return OutgoingEmailServiceImpl.validateEmailAddress(emailAddress);
  }
}
