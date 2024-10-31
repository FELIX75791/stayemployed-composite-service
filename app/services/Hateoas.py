
class Hateoas:
  def __init__(self, user_code, application_code, update_code):
    self.dashboard_link = {"rel": "dashboard", "href": "/dashboard"}
    self.changeStatus_link = {"rel": "update", "href": "/changeStatus"}
    self.applyJobs_link = {"rel": "apply", "href": "/applyJobs"}
    self.user_code = user_code
    self.application_code = application_code
    self.update_code = update_code
    
  def can_dashboard(self):
    return self.application_code == 200 or self.update_code == 200 or self.update_code == 404

  def can_apply_jobs(self):
    return self.user_code == 200 or self.update_code == 200 or self.update_code == 404
 
  def can_update_status(self):
    if self.application_code == 200:
      return True
    if self.application_code != 200:
      return False

    # return self.user_code == 200 or self.application_code == 200

  def generate_hateoas(self, self_href):
      result = []
      self_link = {"rel": "self", "href": self_href}
      result.append(self_link)
      if self_href != "/dashboard" and self.can_dashboard():
        result.append(self.dashboard_link)
      if self_href != "/applyJobs" and self.can_apply_jobs():
        result.append(self.applyJobs_link)
      if self_href != "/changeStatus" and self.can_update_status():
        result.append(self.changeStatus_link)
      
      return result
